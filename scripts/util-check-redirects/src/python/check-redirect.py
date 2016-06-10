#!/usr/bin/env python
'''
A fast script for checking a list of URLs
'''
import csv
import sys
import urllib, urllib2

""" A Sample handler for urllib2
    Prevent default behavior of following redirects.  Will capture and return the redirect information insteead
"""
class NoRedirect(urllib2.HTTPRedirectHandler):
    # Capture and return the forward information
    def http_error_302(self, req, fp, code, msg, headers):
        #pass
        infourl = urllib.addinfourl(fp, headers, req.get_full_url())
        infourl.status = code
        infourl.code = code
        return infourl


"""A utility helper to check on HTTP requests"""
class HttpChecker:
    def __init__(self):
        self.source = ""

    ''' Load the list of URLs to check from given CSV file
        @return List
    '''
    def loadCsvList(self, sFilename):
        oCheckList = []
        try:
            oFile = open(sFilename, "r")
        except IOError:
            print "Count not open file: " + sFilename
        except:
            print("Unexpected: ", sys.exc_info()[0])
            raise
        else:
            import csv
            dialect = csv.Sniffer().sniff(oFile.read(1024))
            oFile.seek(0)
            reader = csv.reader(oFile, dialect)
            for row in reader:
                sCode = 301
                if row[2][0].upper() == "F": # NOT temporary
                    sCode = 302
                oCheckList.append({"origin": row[0], "redirect": row[1], "code": sCode})
            oFile.close()
        return oCheckList

    def check(self):
        print "..... Start checking...."
        sFilename = "config.csv"
        oCheckList = self.loadCsvList(sFilename);
        oOpener = urllib2.build_opener(NoRedirect())
        for oCheck in oCheckList:
            oResponse = oOpener.open(oCheck["origin"])
            sRedirectLoation = None
            print "testing URL: " + oCheck["origin"]
            # Compare response code
            if oCheck["code"] != oResponse.getcode():
                print "xxxx    Bad response code: expects " + str(oCheck["code"]) + " got " + str(oResponse.getcode())
            # Compare the redirect location
            try:
                sRedirectLoation = oResponse.headers["Location"]
            except:
                print "xxxx    Bad final location: expects " + str(oCheck["redirect"]) + " got NO redirect location available"
                pass
            else:
                if oCheck["redirect"] != sRedirectLoation:
                    print "xxxx    Bad final location: expects " + str(oCheck["redirect"]) + " got " + str(sRedirectLoation)

# Main function call
oChecker = HttpChecker()
oChecker.check()
