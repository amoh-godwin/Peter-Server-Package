# -*- coding: utf-8 -*-
# To You Alone Oh Father, I commit myself
import os
import chardet
from time import time
from external import PHPRunner
from css_fs import CssRunner
from py_fs import PyRunner

class FileSystem():


    """
    File system
    sets the actual file name (folders are treated as files)
    sets the file type
    returns the encoding
    returns the data
    """


    def __init__(self):


        super.__self__
        self.request_method = ''
        self.Default_LOCATION = "C:/Deuteronomy Works/Peter/Server"
        self.status_code = 200
        self.additional_head_str = {}
        self._actual_file = ''
        self.query_string = ''
        self.post_data = ''
        self._no = 0
        self._steps = []
        self._depth = 0
        self.SCRIPTS_LOCATION = "C:/Deuteronomy Works/Peter/_scripts"
        self._file_extension = 'html'
        self.mime_video_type = [
                '1d-interleaved-parityfec', '3gpp', '3gpp2'
                '3gpp-tt', 'BMPEG', 'BT656', 'CelB', 'DV', 'encaprtp',
                'example', 'flexfec', 'H261', 'H263', 'H263-1998', 'H263-2000',
                'H264', 'H264-RCDO', 'H264-SVC', 'H265', 'iso.segment', 'JPEG',
                'jpeg2000', 'mj2', 'MP1S', 'MP2P', 'MP2T', 'mp4', 'MP4V-ES',
                'MPV', 'mpeg', 'mpeg4-generic', 'nv', 'ogg', 'parityfec',
                'pointer', 'quicktime', 'raptorfec', 'raw', 'rtp-enc-aescm128',
                'rtploopback', 'rtx', 'smpte291', 'SMPTE292M', 'ulpfec', 'vc1',
                'vc2', 'vnd.CCTV', 'vnd.dece.hd', 'vnd.dece.mobile',
                'vnd.dece.mp4', 'vnd.dece.pd', 'vnd.dece.sd', 'vnd.dece.video',
                'vnd.directv.mpeg', 'vnd.directv.mpeg-tts',
                'vnd.dlna.mpeg-tts', 'vnd.dvb.file', 'vnd.fvt',
                'vnd.hns.video', 'vnd.iptvforum.1dparityfec-1010',
                'vnd.iptvforum.1dparityfec-2005',
                'vnd.iptvforum.2dparityfec-1010',
                'vnd.iptvforum.2dparityfec-2005', 'vnd.iptvforum.ttsavc',
                'vnd.iptvforum.ttsmpeg2', 'vnd.motorola.video',
                'vnd.motorola.videop', 'vnd.mpegurl',
                'vnd.ms-playready.media.pyv',
                'vnd.nokia.interleaved-multimedia', 'vnd.nokia.mp4vr',
                'vnd.nokia.videovoip', 'vnd.objectvideo',
                'vnd.radgamettools.bink', 'vnd.radgamettools.smacker',
                'vnd.sealed.mpeg1', 'vnd.sealed.mpeg4', 'vnd.sealed.swf',
                'vnd.sealedmedia.softseal.mov', 'vnd.uvvu.mp4',
                'vnd.youtube.yt', 'vnd.vivo', 'VP8']
        self.mime_app_type = [
                "1d-interleaved-parityfec", "3gpdash-qoe-report+xml", "3gpp-ims+xml",
                "A2L", "activemessage", "activity+json", "alto-costmap+json", "alto-costmapfilter+json",
                "alto-directory+json", "alto-endpointprop+json", "alto-endpointpropparams+json",
                "alto-endpointcost+json", "alto-endpointcostparams+json", "alto-error+json",
                "alto-networkmapfilter+json", "alto-networkmap+json", "AML", "andrew-inset",
                "applefile", "ATF", "ATFX", "atom+xml", "atomcat+xml", "atomdeleted+xml", "atomicmail",
                "atomsvc+xml", "atsc-dwd+xml", "atsc-held+xml", "atsc-rsat+xml", "ATXML", "auth-policy+xml", "bacnet-xdd+zip",
                "batch-SMTP", "beep+xml", "calendar+json", "calendar+xml", "call-completion", "CALS-1840", "cbor",
                "cbor", "cccex", "ccmp+xml", "ccxml+xml", "CDFX+XML", "cdmi-capability", "cdmi-container",
                "cdmi-domain", "cdmi-object", "cdmi-queue", "cdni", "CEA", "cea-2018+xml", "cellml+xml",
                "cfw", "clue_info+xml", "cms", "cnrp+xml", "coap-group+json", "coap-payload", "commonground",
                "conference-info+xml", "cpl+xml", "cose", "cose-key", "cose-key-set", "csrattrs", "csta+xml",
                "CSTAdata+xml", "csvm+json", "cwt", "cybercash",
                "dash+xml", "dashdelta", "davmount+xml", "dca-rft",
                "DCD", "dec-dx", "dialog-info+xml", "dicom",
                "dicom+json", "dicom+xml", "DII", "DIT",
                "dns", "dns+json", "dns-message", "dskpp+xml",
                "dssc+der", "dssc+xml", "dvcs", "ecmascript",
                "EDI-consent", "EDIFACT", "EDI-X12", "efi",
                "EmergencyCallData.Comment+xml", "EmergencyCallData.Control+xml",
                "EmergencyCallData.DeviceInfo+xml", "EmergencyCallData.eCall.MSD",
                "EmergencyCallData.ProviderInfo+xml", "EmergencyCallData.ServiceInfo+xml",
                "EmergencyCallData.SubscriberInfo+xml", "EmergencyCallData.VEDS+xml",
                "emma+xml", "emotionml+xml", "encaprtp", "epp+xml",
                "epub+zip", "eshop", "example", "exi",
                "expect-ct-report+json", "fastinfoset", "fastsoap", "fdt+xml",
                "fhir+json", "fhir+xml", "fits", "flexfec", "font-tdpfr",
                "framework-attributes+xml", "geo+json", "geo+json-seq",
                "geopackage+sqlite3", "geoxacml+xml",
                "gltf-buffer", "gml+xml", "gzip", "H224", "held+xml",
                "http", "hyperstudio", "ibe-key-request+xml", "ibe-pkg-reply+xml", "ibe-pp-data",
                "iges", "im-iscomposing+xm", "index", "index.cmd", "index.obj",
                "index.response", "index.vnd", "inkml+xml", "IOTP", "ipfix",
                "ipp", "isup", "its+xml", "javascript", "json", "jf2feed+json",
                "jose", "jose+json", "jrd+json", "json-patch+json",
                "json-seq", "jwk+json",
                "jwk-set+json", "jwt", "kpml-request+xml", "kpml-response+xml",
                "ld+json", "lgr+xml", "link-format", "load-control+xml",
                "lost+xml", "lostsync+xml",
                "LXF", "mac-binhex40", "macwriteii", "mads+xml", "marc", "marcxml+xml",
                "mathematica", "mathml-content+xml", "mathml-presentation+xml",
                "mathml+xml", "mbms-associated-procedure-description+xml",
                "mbms-deregister+xml", "mbms-envelope+xml",
                "mbms-msk-response+xml", "mbms-msk+xml",
                "mbms-protection-description+xml", "mbms-reception-report+xml",
                "mbms-register-response+xml", "mbms-register+xml", "mbms-schedule+xml",
                "mbms-user-service-description+xml", "mbox",
                "media_control+xml", "media-policy-dataset+xml",
                "mediaservercontrol+xml", "merge-patch+json", "metalink4+xml",
                "mets+xml", "MF4", "mikey", "mipc",
                "mmt-aei+xml", "mmt-usd+xml", "mods+xml", "moss-keys",
                "moss-signature", "mosskey-data", "mosskey-request",
                "mp21", "mp4", "mpeg4-generic", "mpeg4-iod", "mpeg4-iod-xmt",
                "mrb-consumer+xml", "mrb-publish+xml", "msc-ivr+xml",
                "msc-mixer+xml", "msword", "mud+json", "mxf", "n-quads",
                "n-triples", "nasdata", "news-checkgroups", "news-groupinfo",
                "news-transmission", "nlsml+xml", "node", "nss", "ocsp-request",
                "ocsp-response", "octet-stream", "ODA",
                "odm+xml", "ODX", "oebps-package+xml", "ogg", "oscore", "oxps",
                "p2p-overlay+xml", "parityfec",
                "passport", "patch-ops-error+xml", "pdf", "PDX",
                "pem-certificate-chain", "pgp-encrypted", "pgp-keys", "pgp-signature",
                "pidf-diff+xml", "pidf+xml", "pkcs10", "pkcs7-mime",
                "pkcs7-signature", "pkcs8", "pkcs8-encrypted", "pkcs12",
                "pkix-attr-cert", "pkix-cert", "pkix-crl", "pkix-pkipath",
                "pkixcmp", "pls+xml", "poc-settings+xml", "postscript",
                "ppsp-tracker+json", "problem+json", "problem+xml", "provenance+xml",
                "prs.alvestrand.titrax-sheet", "prs.cww", "prs.hpub", "prs.nprend",
                "prs.plucker", "prs.rdf-xml-crypt", "prs.xsf", "pskc+xml",
                "rdf+xml", "route-apd+xml", "route-s-tsid+xml", "route-usd+xml",
                "QSIG", "raptorfec", "rdap+json", "reginfo+xml",
                "relax-ng-compact-syntax", "remote-printing", "reputon+json",
                "resource-lists-diff+xml", "resource-lists+xml", "rfc+xml",
                "riscos", "rlmi+xml", "rls-services+xml", "rpki-ghostbusters",
                "rpki-manifest", "rpki-publication", "rpki-roa", "rpki-updown",
                "rtf", "rtploopback", "rtx", "samlassertion+xml", "samlmetadata+xml",
                "sbml+xml", "scaip+xml", "scim+json",
                "scvp-cv-request", "scvp-cv-response", "scvp-vp-request",
                "scvp-vp-response", "sdp", "secevent+jwt", "senml-exi",
                "senml+cbor", "senml+json", "senml+xml", "sensml-exi",
                "sensml+cbor", "sensml+json", "sensml+xml", "sep-exi",
                "sep+xml", "session-info", "set-payment",
                "set-payment-initiation", "set-registration",
                "set-registration-initiation", "sgml", "sgml-open-catalog",
                "shf+xml", "sieve", "simple-filter+xml", "simple-message-summary",
                "simpleSymbolContainer", "sipc", "slate", "smil+xml",
                "smpte336m", "soap+fastinfoset", "soap+xml", "sparql-query",
                "sparql-results+xml", "spirits-event+xml",
                "sql", "srgs", "srgs+xml", "sru+xml", "ssml+xml", "stix+json",
                "swid+xml", "tamp-apex-update", "tamp-apex-update-confirm",
                "tamp-community-update", "tamp-community-update-confirm",
                "tamp-error", "tamp-sequence-adjust",
                "tamp-sequence-adjust-confirm", "tamp-status-query",
                "tamp-status-response", "tamp-update",
                "tamp-update-confirm", "taxii+json", "tei+xml", "TETRA_ISI",
                "thraud+xml", "timestamp-query", "timestamp-reply",
                "timestamped-data", "tlsrpt+gzip", "tlsrpt+json",
                "tnauthlist", "trickle-ice-sdpfrag", "trig", "ttml+xml",
                "tve-trigger", "tzif", "tzif-leap", "ulpfec",
                "urc-grpsheet+xml", "urc-ressheet+xml",
                "urc-targetdesc+xml", "urc-uisocketdesc+xml", "vcard+json",
                "vcard+xml", "vemmi"]

        self.mime_image_type = [
                                "png", "jpeg", "gif", "tiff",
                                "aces", "avci", "avcs", "bmp", "cgm",
                                "dicom-rle", "emf", "example", "fits",
                                "g3fax", "heic", "heic-sequence", "heif",
                                "heif-sequence", "hej2k", "hsj2", "ief", "jls",
                                "jp2", "jph", "jphc", "jpm", "jpx",
                                "jxr", "jxrA", "jxrS", "jxs",
                                "jxsc", "jxsi", "jxss", "ktx",
                                "naplps", "prs.btif", "prs.pti", "pwg-raster",
                                "svg", "t38", "tiff-fx",
                                "vnd.adobe.photoshop",
                                "vnd.airzip.accelerator.azv", "vnd.cns.inf2",
                                "vnd.dece.graphic", "vnd.djvu", "vnd.dwg",
                                "vnd.dxf", "vnd.dvb.subtitle",
                                "vnd.fastbidsheet", "vnd.fpx", "vnd.fst",
                                "vnd.fujixerox.edmics-mmr",
                                "vnd.fujixerox.edmics-rlc",
                                "vnd.globalgraphics.pgb", "vnd.microsoft.icon",
                                "vnd.mix", "vnd.ms-modi",
                                "vnd.mozilla.apng", "vnd.net-fpx",
                                "vnd.radiance", "vnd.sealed.png",
                                "vnd.sealedmedia.softseal.gif",
                                "vnd.sealedmedia.softseal.jpg", "vnd.svf",
                                "vnd.tencent.tap", "vnd.valve.source.texture",
                                "vnd.wap.wbmp", "vnd.xiff", "vnd.zbrush.pcx",
                                "wmf", "emf"]
        self.data = ''
        self.encoding = 'ascii'
        self.contentLength = 0


    def _getFileName(self, requested_file):


        # first split to reveal query if any
        # query will be in the second one without the '?' if any
        splits = requested_file.split('?')

        # query should be here
        if len(splits) > 1:
            self.query_string = splits[1]

        # whether or not is a query we are still taken the file only
        self._actual_file = splits[0]

        if self._actual_file == '/':
            pass
        else:
            # the extension will be in the last one
            split = self._actual_file.split('.')
            self._file_extension = split[-1]


    def search(self, file):


        # call to find actual file name
        self._getFileName(file)
 
        # this are the steps we'll use and depth we have to go
        self._steps = self._actual_file.split('/')

        # some clean ups
        del self._steps[0]

        # the depth of the path
        self._depth = len(self._steps)

        # try to open the file
        try:

            # try to find oepn file here
            # INITIALISE THE COUNTER
            self._no = 0

            if self._steps[self._no] == '':
                self._to_list(self.Default_LOCATION)

            else:

                # call
                folders = os.listdir(self.Default_LOCATION)
                if self._steps[self._no] in folders:

                    # if that step is here then we continue
                    item = self.Default_LOCATION + '/' + self._steps[self._no]

                    if self._is_dir(item):

                        # check if blank ''
                        self._is_blank(item)

                    else:

                        # its a file return it
                        self._data(item)

                else:

                    # will couldn't find the file in the nest
                    self.status_code = 404
                    return self.status_code

            # status code found
            return self.status_code

        except:

            # status code not found
            self.status_code = 404
            return self.status_code


    def _crawl(self, path, needle):


        folders = os.listdir(path)
        if needle in folders:

            # make new path
            item = path + '/' + needle

            # find if is file or dir
            if self._is_dir(item):

                # continue crawling is a dir
                self._is_blank(item)

            else:

                # return, it is a file
                # data will be ready in self.data
                self._data(item)

        else:

            # we couldn't find it means we have ended
            self.status_code = 404
            return

    def _is_blank(self, path):

        # depths
        self._no += 1

        # check if the current no is not blank
        if self._no == self._depth:

            self._to_list(path)

        elif self._steps[self._no] != '':

            # crawl again
            # needle is second param
            self._crawl(path, self._steps[self._no])

        else:

            # to dir listing or index.html
            self._to_list(path + '/' + self._steps[self._no])


    def _is_dir(self, path):
        try:
            os.listdir(path)
            return True
        except:
            return False


    def _to_list(self, path):


        """
        checks whether this particular path has an index file in it
        or Peter should go ahead and check the .htaccess for listing perm.
        """


        files = os.listdir(path)

        if 'index.php' in files:

            # file extension sure contains gibberish
            self._file_extension = 'php'

            # call self._data to handle
            self._data(path + '/index.php')

        elif 'index.html' in files:

            # file extension sure contains gibberish
            self._file_extension = 'html'

            # call self.data to handle
            self._data(path + '/index.html')

        elif '.htaccess' in files:

            # file extension sure contains gibberish
            self._file_extension = 'html'

            # call to permission reader
            with open(path + '/.htaccess', mode='rb') as ht:
                data = ht.read()

            # working on the file line by line
            if b'Options -Indexes' in data:

                # returnt the 403 document instead
                self._data(self.SCRIPTS_LOCATION + '/403.html')

            else:

                # sure we're going to list
                self._data(self.SCRIPTS_LOCATION + '/dir.html')

        else:

            # file extension sure contains gibberish
            #self._file_extension = 'php' 

            # htacces or just go ahead to list dir
            self._data(self.SCRIPTS_LOCATION + '/dir.html' )


    def _data(self, file):

        start_time = time()
        # check the file extension for php
        if self._file_extension == 'py':

            pyrunner = PyRunner()
            read = pyrunner.start(file)
            
            # return values
            self.contentLength = len(read)
            self.encoding = pyrunner.encoding
            self.data = read
            return

        if self._file_extension == 'php':

            # setting the directory to directory
            phpRunner = PHPRunner()

            # run with php and with the query
            phpRunner.encoding = self.encoding
            phpRunner.post_data = self.post_data
            read = phpRunner.Start(file, self.query_string, self.request_method)
            self.additional_head_str = phpRunner.addition_head_str

            # set length of the content
            self.contentLength = len(read)
            self.encoding = phpRunner.encoding
            self.data = read
            return

        elif self._file_extension == 'css':

            # The file is a css file
            Css = CssRunner()
            read = Css.Read(file)
            self.contentLength = len(read)
            self.data = read
            return

        elif self._file_extension in self.mime_image_type:

            end_time = time()
            print(end_time)
            space = end_time - start_time
            print('sec: ', space)
            # It is an image file defined in self.mime_types['image']
            with open(file, 'rb') as bbin:
                read = bbin.read()
            self.data = read
            self.contentLength = len(read)
            return

        else:

            # file is not php
            with open(file, 'rb') as bbin:
                read = bbin.read()

                # set length of the content
                self.contentlength = len(read)

        # Continue with encoding detection
        ## Use only 128 bytes to speed things up
        count = 0
        to_send_bytes = b''
        split_bytes = read.splitlines(keepends=True)
        for each in split_bytes:
            if count < 128:
                to_send_bytes += each
                count += 1

        detection = chardet.detect(to_send_bytes)
        print(detection)

        if detection['confidence'] > 0.99:
            self.encoding = detection['encoding']

        # if detection in none
        elif detection['confidence'] < 0.1:
            self.data = read
            self.contentLength = len(read)
    
            # it should return, nothing else to do
            return
        else:
            self.encoding = 'ascii'

        self.data = read.decode(self.encoding)

        return
