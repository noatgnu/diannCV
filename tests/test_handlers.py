import tornado.testing
from tornado.escape import json_encode
from tornado.httpclient import AsyncHTTPClient
from tornado.testing import AsyncTestCase


class TestUniprotHandler(AsyncTestCase):
    @tornado.testing.gen_test
    def test_post(self):
        client = AsyncHTTPClient()
        data = {
            "id": "test",
            "file": r"//mrc-smb.lifesci.dundee.ac.uk/mrc-group-folder/ALESSI/Toan/For DIANN CV/Reports.pr_matrix.tsv",
            "filename": "report.pg_matrix.tsv",
            "conditions": {'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT_IP_01_S1-A1_1_1839.d': 'Old-Lung-LT_IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT_IP_02_S1-A2_1_1840.d': 'Old-Lung-LT_IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT_IP_03_S1-A3_1_1841.d': 'Old-Lung-LT_IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT_IP_04_S1-A4_1_1842.d': 'Old-Lung-LT_IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT_IP_05_S1-A5_1_1843.d': 'Old-Lung-LT_IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT-WCL_01_S1-B5_1_1855.d': 'Old-Lung-LT-WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT-WCL_02_S1-B6_1_1856.d': 'Old-Lung-LT-WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT-WCL_03_S1-B7_1_1857.d': 'Old-Lung-LT-WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT-WCL_04_S1-B8_1_1858.d': 'Old-Lung-LT-WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT-WCL_05_S1-B9_1_1859.d': 'Old-Lung-LT-WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT_WCL_01_S1-B10_1_1860.d': 'Old-Lung-WT_WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT_WCL_02_S1-B11_1_1861.d': 'Old-Lung-WT_WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT_WCL_03_S1-B12_1_1862.d': 'Old-Lung-WT_WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT_WCL_04_S1-C1_1_1863.d': 'Old-Lung-WT_WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT-IP_01_S1-A6_1_1844.d': 'Old-Lung-WT-IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT-IP_02_S1-A7_1_1845.d': 'Old-Lung-WT-IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT-IP_03_S1-A8_1_1846.d': 'Old-Lung-WT-IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT-IP_04_S1-A9_1_1847.d': 'Old-Lung-WT-IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT_WCL_01_S1-C2_1_1864.d': 'Young-Lung-LT_WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT_WCL_02_S1-C3_1_1865.d': 'Young-Lung-LT_WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT_WCL_03_S1-C4_1_1866.d': 'Young-Lung-LT_WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT_WCL_04_S1-C5_1_1867.d': 'Young-Lung-LT_WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT-IP_01_S1-A10_1_1848.d': 'Young-Lung-LT-IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT-IP_02_S1-A11_1_1849.d': 'Young-Lung-LT-IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT-IP_03_S1-A12_1_1850.d': 'Young-Lung-LT-IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT-IP_04_S1-B1_1_1851.d': 'Young-Lung-LT-IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-WT_WCL_01_S1-C6_1_1868.d': 'Young-Lung-WT_WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-WT_WCL_02_S1-C7_1_1869.d': 'Young-Lung-WT_WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-WT_WCL_03_S1-C8_1_1870.d': 'Young-Lung-WT_WCL', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-WT-IP_01_S1-B2_1_1852.d': 'Young-Lung-WT-IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-WT-IP_02_S1-B3_1_1853.d': 'Young-Lung-WT-IP', 'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-WT-IP_03_S1-B4_1_1854.d': 'Young-Lung-WT-IP'}
,
            "extra": {
                "minimumGoodConditions": 2,
                "minimumGoodSamples": 2
            }
        }
        #data["acc"] = data["acc"][:3]
        response = yield client.fetch(
            "http://localhost:8000/processFile",
            method="POST",
            headers={"Content-Type": "application/x-json"},
            body=json_encode(data))
        print(response.body)

    @tornado.testing.gen_test
    def test_post3(self):
        client = AsyncHTTPClient()
        data = {
            "id": "test",
            "file": r"//mrc-smb.lifesci.dundee.ac.uk/mrc-group-folder/ALESSI/Toan/For DIANN CV/Reports.tsv",
            "filename": "report.tsv",
            "conditions": {
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT_IP_01_S1-A1_1_1839.d': 'Old-Lung-LT_IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT_IP_02_S1-A2_1_1840.d': 'Old-Lung-LT_IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT_IP_03_S1-A3_1_1841.d': 'Old-Lung-LT_IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT_IP_04_S1-A4_1_1842.d': 'Old-Lung-LT_IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT_IP_05_S1-A5_1_1843.d': 'Old-Lung-LT_IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT-WCL_01_S1-B5_1_1855.d': 'Old-Lung-LT-WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT-WCL_02_S1-B6_1_1856.d': 'Old-Lung-LT-WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT-WCL_03_S1-B7_1_1857.d': 'Old-Lung-LT-WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT-WCL_04_S1-B8_1_1858.d': 'Old-Lung-LT-WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-LT-WCL_05_S1-B9_1_1859.d': 'Old-Lung-LT-WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT_WCL_01_S1-B10_1_1860.d': 'Old-Lung-WT_WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT_WCL_02_S1-B11_1_1861.d': 'Old-Lung-WT_WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT_WCL_03_S1-B12_1_1862.d': 'Old-Lung-WT_WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT_WCL_04_S1-C1_1_1863.d': 'Old-Lung-WT_WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT-IP_01_S1-A6_1_1844.d': 'Old-Lung-WT-IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT-IP_02_S1-A7_1_1845.d': 'Old-Lung-WT-IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT-IP_03_S1-A8_1_1846.d': 'Old-Lung-WT-IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Old-Lung-WT-IP_04_S1-A9_1_1847.d': 'Old-Lung-WT-IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT_WCL_01_S1-C2_1_1864.d': 'Young-Lung-LT_WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT_WCL_02_S1-C3_1_1865.d': 'Young-Lung-LT_WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT_WCL_03_S1-C4_1_1866.d': 'Young-Lung-LT_WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT_WCL_04_S1-C5_1_1867.d': 'Young-Lung-LT_WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT-IP_01_S1-A10_1_1848.d': 'Young-Lung-LT-IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT-IP_02_S1-A11_1_1849.d': 'Young-Lung-LT-IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT-IP_03_S1-A12_1_1850.d': 'Young-Lung-LT-IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-LT-IP_04_S1-B1_1_1851.d': 'Young-Lung-LT-IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-WT_WCL_01_S1-C6_1_1868.d': 'Young-Lung-WT_WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-WT_WCL_02_S1-C7_1_1869.d': 'Young-Lung-WT_WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-WT_WCL_03_S1-C8_1_1870.d': 'Young-Lung-WT_WCL',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-WT-IP_01_S1-B2_1_1852.d': 'Young-Lung-WT-IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-WT-IP_02_S1-B3_1_1853.d': 'Young-Lung-WT-IP',
                'C:\\Raja\\DIA-NN searches\\LT-Lung_Aging_All02\\20211117_RN_Young-Lung-WT-IP_03_S1-B4_1_1854.d': 'Young-Lung-WT-IP'}
            ,
            "extra": {
                "minimumGoodConditions": 2,
                "minimumGoodSamples": 2
            }
        }
        # data["acc"] = data["acc"][:3]
        response = yield client.fetch(
            "http://localhost:8000/processFile",
            method="POST",
            headers={"Content-Type": "application/x-json"},
            body=json_encode(data))
        print(response.body)

    @tornado.testing.gen_test
    def test_post2(self):
        client = AsyncHTTPClient()
        data = {
            "id": "test",
            "file": "//mrc-smb.lifesci.dundee.ac.uk/mrc-group-folder/ALESSI/Toan/BGX001_OBG_easypqplib/report.tsv",
            "filename": "report.tsv",
            "conditions": {
                r"C:\Beth\RAW\20211021\BG_211021_BGX001_OBD_DIAPASEF_169_1_S2-A12_1_1396.d": "165-167-168-169",
                r"C:\Beth\RAW\20211021\BG_211021_BGX001_OBD_DIAPASEF_167_1_S2-A10_1_1394.d": "165-167-168-169",
                r"C:\Beth\RAW\20211021\BG_211021_BGX001_OBD_DIAPASEF_165_1_S2-A8_1_1392.d": "165-167-168-169",
                r"C:\Beth\RAW\20211021\BG_211021_BGX001_OBD_DIAPASEF_168_1_S2-A11_1_1395.d": "165-167-168-169",
                r"C:\Beth\RAW\20211021\BG_211021_BGX001_OBD_DIAPASEF_166_1_S2-A9_1_1393.d": "164-166",
                r"C:\Beth\RAW\20211021\BG_211021_BGX001_OBD_DIAPASEF_164_1_S2-A7_1_1391.d": "164-166",
            },
            "extra": {
                "minimumGoodConditions": 2,
                "minimumGoodSamples": 2
            }
        }
        #data["acc"] = data["acc"][:3]
        response = yield client.fetch(
            "http://localhost:8000/processFile",
            method="POST",
            headers={"Content-Type": "application/x-json"},
            body=json_encode(data))
        print(response.body)