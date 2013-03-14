from __future__ import print_function
import simplejson as json
import h5py
import numpy
import scipy
import scipy.io
import os

class JSON_Converter(object):

    def __init__(self,jsonFileName):
        self.jsonFileName = jsonFileName
        self.jsonData = None
        self.dictOfArrays = None
        self.readFile()

    def writeMatFile(self,matFileName=None):
        assert self.dictOfArrays is not None, 'dictOfArrays is None'
        if matFileName is None:
            matFileName = self.getAutoFileName(ext='mat')
        dataDict = dict(self.dictOfArrays)
        dataDict['json_file'] = self.jsonFileName
        scipy.io.savemat(matFileName, {'data': dataDict}, oned_as='row')
            
    def writeH5File(self,h5FileName=None):
        assert self.dictOfArrays is not None, 'dictOfArrays is None'
        if h5FileName is None:
            h5FileName = self.getAutoFileName(ext='hdf5')

        h5File = h5py.File(h5FileName,'w')
        dataGroup = h5File.create_group('/data')
        dataGroup.attrs['json_file'] =  self.jsonFileName

        for k, v in self.dictOfArrays.iteritems():
            if type(v) == numpy.ndarray:
                maxshape = (None,)*len(v.shape)
                dataSet = dataGroup.create_dataset(k, v.shape, data=v, dtype=v.dtype, maxshape=maxshape)
            elif type(v) == dict:
                subGroup = dataGroup.create_group(k)
                for kk, vv in v.iteritems():
                    maxshape = (None,)*len(vv.shape)
                    dataSet = subGroup.create_dataset(kk, vv.shape, data=vv, dtype=vv.dtype, maxshape=maxshape)
            elif type(v) == list:
                dtype = h5py.special_dtype(vlen=str)
                dataSet = dataGroup.create_dataset(k,(len(v),), data=v, dtype=dtype, maxshape=(None,))

            else:
                errorMsg = 'unexpected type, {0}, in dictOfArrays when creating hdf5 file'.format(type(v))
                raise RuntimeError,  errorMsg 

        h5File.close()

    def getAutoFileName(self,ext):
        baseName, jsonExt = os.path.splitext(self.jsonFileName)
        autoFileName = '{0}.{1}'.format(baseName,ext)
        return autoFileName

    def readFile(self):
        with open(self.jsonFileName,'r') as f:
            self.jsonData = json.load(f)
        self.jsonDataToDictOfArrays()

    def jsonDataToDictOfArrays(self):
        assert self.jsonData is not None, 'jsonData is None'

        self.dictOfArrays = {}
        dataLength = len(self.jsonData)

        # Initialize arrays based on first item in list
        for k,v in self.jsonData[0].iteritems():
            k = str(k)
            if ('pts' in k) or ('bndry' in k) or ('midpt' in k):
                if type(v) != list:
                    v = [v]
                self.dictOfArrays[k] = {}
                for i in range(len(v)):
                    point = 'p{0}'.format(i+1)
                    self.dictOfArrays[k][point] = scipy.zeros((dataLength,2), dtype=scipy.float64)
            else:
                if type(v) == str or type(v) == unicode:
                    self.dictOfArrays[k] = []
                else:
                    if type(v) == int:
                        dtype = scipy.int64
                    elif type(v) == float:
                        dtype = scipy.float64
                    elif type(v) == bool:
                        dtype = scipy.int64
                        v = int(v)
                    else:
                        raise ValueError, 'unsupported type, {0}, for {1}'.format(type(v),k)
                    self.dictOfArrays[k] = scipy.zeros((dataLength,), dtype=dtype)

        # Add array for camera numbers
        self.dictOfArrays['camera_number'] = scipy.zeros((dataLength,), dtype=scipy.int64)

        # Add data to arrays
        for i, item in enumerate(self.jsonData):
            for k,v in item.iteritems():
                k = str(k)
                if ('pts' in k) or ('bndry' in k) or ('midpt' in k):
                    if type(v) != list:
                        v = [v]
                    for j, subItem in enumerate(v):
                        point = 'p{0}'.format(j+1)
                        self.dictOfArrays[k][point][i,0] = subItem['x']
                        self.dictOfArrays[k][point][i,1] = subItem['y']
                else:
                    if type(v) == str or type(v) == unicode:
                        v=str(v)
                        self.dictOfArrays[k].append(v)
                        if k == 'camera':
                            dummy, numStr = v.split('_')
                            self.dictOfArrays['camera_number'][i] = int(numStr)
                    else:
                        self.dictOfArrays[k][i]  = v

        # Add double base time array - for convenience
        sec = self.dictOfArrays['secs']
        nsec = self.dictOfArrays['nsecs']
        self.dictOfArrays['time'] = sec.astype(scipy.double) 
        self.dictOfArrays['time'] += (1.0e-9)*nsec.astype(scipy.double)
        self.dictOfArrays['time'] -= self.dictOfArrays['time'][0]




# -----------------------------------------------------------------------------
if __name__ == '__main__':
    jsonfileName = 'maze_tracking_pts_logger_20130108T153110copy.json' 
    converter = JSON_Converter(jsonfileName)
    converter.writeMatFile()
    converter.writeH5File()






