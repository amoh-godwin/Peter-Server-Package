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
        self.mime_font_type = [
                'collection', 'otf', 'sfnt', 'ttf', 'woff', 'woff2']

        self.mime_audio_type = [
                '1d-interleaved-parityfec', '32kadpcm', '3gpp', '3gpp2', 'aac',
                'ac3', 'AMR', 'AMR-WB', 'amr-wb+', 'aptx', 'asc',
                'ATRAC-ADVANCED-LOSSLESS', 'ATRAC-X', 'ATRAC3', 'basic',
                'BV16', 'BV32', 'clearmode', 'CN', 'DAT12', 'dls',
                'dsr-es201108', 'dsr-es202050', 'dsr-es202211', 'dsr-es202212',
                'DV', 'DVI4', 'eac3', 'encaprtp', 'EVRC', 'EVRC-QCP', 'EVRC0',
                'EVRC1', 'EVRCB', 'EVRCB0', 'EVRCB1', 'EVRCNW', 'EVRCNW0',
                'EVRCNW1', 'EVRCWB', 'EVRCWB0', 'EVRCWB1', 'EVS', 'example',
                'flexfec', 'fwdred', 'G711-0', 'G719', 'G7221', 'G722', 'G723',
                'G726-16', 'G726-24', 'G726-32', 'G726-40', 'G728', 'G729',
                'G7291', 'G729D', 'G729E', 'GSM', 'GSM-EFR', 'GSM-HR-08',
                'iLBC', 'ip-mr_v2.5', 'L8', 'L16', 'L20', 'L24', 'LPC',
                'MELP', 'MELP600', 'MELP1200', 'MELP2400', 'mobile-xmf', 'MPA',
                'mp4', 'MP4A-LATM', 'mpa-robust', 'mpeg', 'mpeg4-generic',
                'ogg', 'opus', 'parityfec', 'PCMA', 'PCMA-WB', 'PCMU',
                'PCMU-WB', 'prs.sid', 'QCELP', 'raptorfec', 'RED',
                'rtp-enc-aescm128', 'rtploopback', 'rtp-midi', 'rtx', 'SMV',
                'SMV0', 'SMV-QCP', 'sp-midi', 'speex', 't140c', 't38',
                'telephone-event', 'TETRA_ACELP', 'tone', 'UEMCLIP', 'ulpfec',
                'usac', 'VDVI', 'VMR-WB', 'vnd.3gpp.iufp', 'vnd.4SB',
                'vnd.audiokoz', 'vnd.CELP', 'vnd.cisco.nse',
                'vnd.cmles.radio-events', 'vnd.cns.anp1', 'vnd.cns.inf1',
                'vnd.dece.audio', 'vnd.digital-winds', 'vnd.dlna.adts',
                'vnd.dolby.heaac.1', 'vnd.dolby.heaac.2', 'vnd.dolby.mlp',
                'vnd.dolby.mps', 'vnd.dolby.pl2', 'vnd.dolby.pl2x',
                'vnd.dolby.pl2z', 'vnd.dolby.pulse.1', 'vnd.dra', 'vnd.dts',
                'vnd.dts.hd', 'vnd.dts.uhd', 'vnd.dvb.file', 'vnd.everad.plj',
                'vnd.hns.audio', 'vnd.lucent.voice',
                'vnd.ms-playready.media.pya', 'vnd.nokia.mobile-xmf',
                'vnd.nortel.vbk', 'vnd.nuera.ecelp4800', 'vnd.nuera.ecelp7470',
                'vnd.nuera.ecelp9600', 'vnd.octel.sbc',
                'vnd.presonus.multitrack', 'vnd.rhetorex.32kadpcm', 'vnd.rip',
                'vnd.sealedmedia.softseal.mpeg', 'vnd.vmx.cvsd', 'vorbis',
                'vorbis-config', 'collection', 'otf', 'sfnt', 'ttf', 'woff',
                'woff2']

        self.mime_model_type = [
                '3mf', 'example', 'gltf-binary', 'gltf+json', 'iges', 'mesh',
                'stl', 'vnd.collada+xml', 'vnd.dwf', 'vnd.flatland.3dml',
                'vnd.gdl', 'vnd.gs-gdl', 'vnd.gtw', 'vnd.moml+xml', 'vnd.mts',
                'vnd.opengex', 'vnd.parasolid.transmit.binary',
                'vnd.parasolid.transmit.text',
                'vnd.rosette.annotated-data-model', 'vnd.usdz+zip',
                'vnd.valve.source.compiled-map', 'vnd.vtu', 'vrml', 'x3d-vrml',
                'x3d+fastinfoset', 'x3d+xml']

        self.mime_multipart_type = [
                'alternative', 'appledouble', 'byteranges','digest',
                'encrypted', 'example', 'form-data', 'header-set', 'mixed',
                'multilingual', 'parallel', 'related', 'report', 'signed',
                'vnd.bint.med-plus', 'voice-message', 'x-mixed-replace']

        self.mime_message_type = [
                'CPIM', 'delivery-status', 'disposition-notification',
                'example', 'external-body', 'feedback-report', 'global',
                'global-delivery-status', 'global-disposition-notification',
                'global-headers', 'http', 'imdn+xml', 'partial', 'rfc822',
                's-http', 'sip', 'sipfrag', 'tracking-status', 'vnd.wfa.wsc']

        self.mime_text_type = [
                '1d-interleaved-parityfec', 'cache-manifest', 'calendar',
                'css', 'csv', 'csv-schema', 'dns', 'encaprtp', 'enriched',
                'example', 'flexfec', 'fwdred', 'grammar-ref-list', 'html',
                'jcr-cnd', 'markdown', 'mizar', 'n3', 'parameters','parityfec',
                'plain', 'provenance-notation', 'prs.fallenstein.rst',
                'prs.lines.tag', 'prs.prop.logic', 'raptorfec', 'RED',
                'rfc822-headers', 'richtext', 'rtf', 'rtp-enc-aescm128',
                'rtploopback', 'rtx', 'sgml', 'strings', 't140',
                'tab-separated-values', 'troff', 'turtle', 'ulpfec',
                'uri-list', 'vcard', 'vnd.a', 'vnd.abc', 'vnd.ascii-art',
                'vnd.curl', 'vnd.debian.copyright', 'vnd.DMClientScript',
                'vnd.dvb.subtitle', 'vnd.esmertec.theme-descriptor', 'vnd.fly',
                'vnd.fmi.flexstor', 'vnd.gml', 'vnd.graphviz', 'vnd.hgl',
                'vnd.in3d.3dml', 'vnd.in3d.spot', 'vnd.IPTC.NewsML',
                'vnd.IPTC.NITF', 'vnd.latex-z', 'vnd.motorola.reflex',
                'vnd.ms-mediapackage', 'vnd.net2phone.commcenter.command',
                'vnd.radisys.msml-basic-layout', 'vnd.senx.warpscript',
                'vnd.si.uricatalogue - OBSOLETED by request',
                'vnd.sun.j2me.app-descriptor', 'vnd.sosi',
                'vnd.trolltech.linguist', 'vnd.wap.si', 'vnd.wap.sl',
                'vnd.wap.wml', 'vnd.wap.wmlscript', 'xml',
                'xml-external-parsed-entity']

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

        self.mime_app_type = ['1d-interleaved-parityfec',
                              '3gpdash-qoe-report+xml', '3gpp-ims+xml', 'A2L',
                              'activemessage', 'activity+json',
                              'alto-costmap+json', 'alto-costmapfilter+json',
                              'alto-directory+json', 'alto-endpointprop+json',
                              'alto-endpointpropparams+json',
                              'alto-endpointcost+json',
                              'alto-endpointcostparams+json',
                              'alto-error+json', 'alto-networkmapfilter+json',
                              'alto-networkmap+json', 'AML', 'andrew-inset',
                              'applefile', 'ATF', 'ATFX', 'atom+xml',
                              'atomcat+xml', 'atomdeleted+xml', 'atomicmail',
                              'atomsvc+xml', 'atsc-dwd+xml', 'atsc-held+xml',
                              'atsc-rsat+xml', 'ATXML', 'auth-policy+xml',
                              'bacnet-xdd+zip', 'batch-SMTP', 'beep+xml',
                              'calendar+json', 'calendar+xml',
                              'call-completion', 'CALS-1840', 'cbor', 'cccex',
                              'ccmp+xml', 'ccxml+xml', 'CDFX+XML',
                              'cdmi-capability', 'cdmi-container',
                              'cdmi-domain', 'cdmi-object', 'cdmi-queue',
                              'cdni', 'CEA', 'cea-2018+xml', 'cellml+xml',
                              'cfw', 'clue_info+xml', 'cms', 'cnrp+xml',
                              'coap-group+json', 'coap-payload',
                              'commonground', 'conference-info+xml', 'cpl+xml',
                              'cose', 'cose-key', 'cose-key-set', 'csrattrs',
                              'csta+xml', 'CSTAdata+xml', 'csvm+json', 'cwt',
                              'cybercash', 'dash+xml', 'dashdelta',
                              'davmount+xml', 'dca-rft', 'DCD', 'dec-dx',
                              'dialog-info+xml', 'dicom', 'dicom+json',
                              'dicom+xml', 'DII', 'DIT', 'dns', 'dns+json',
                              'dns-message', 'dskpp+xml', 'dssc+der',
                              'dssc+xml', 'dvcs', 'ecmascript', 'EDI-consent',
                              'EDIFACT', 'EDI-X12', 'efi',
                              'EmergencyCallData.Comment+xml',
                              'EmergencyCallData.Control+xml',
                              'EmergencyCallData.DeviceInfo+xml',
                              'EmergencyCallData.eCall.MSD',
                              'EmergencyCallData.ProviderInfo+xml',
                              'EmergencyCallData.ServiceInfo+xml',
                              'EmergencyCallData.SubscriberInfo+xml',
                              'EmergencyCallData.VEDS+xml', 'emma+xml',
                              'emotionml+xml', 'encaprtp', 'epp+xml',
                              'epub+zip', 'eshop', 'example', 'exi',
                              'expect-ct-report+json', 'fastinfoset',
                              'fastsoap', 'fdt+xml', 'fhir+json', 'fhir+xml',
                              'fits', 'flexfec', 'font-tdpfr',
                              'framework-attributes+xml', 'geo+json',
                              'geo+json-seq', 'geopackage+sqlite3',
                              'geoxacml+xml', 'gltf-buffer', 'gml+xml', 'gzip',
                              'H224', 'held+xml', 'http', 'hyperstudio',
                              'ibe-key-request+xml', 'ibe-pkg-reply+xml',
                              'ibe-pp-data', 'iges', 'im-iscomposing+xml',
                              'index', 'index.cmd', 'index.obj',
                              'index.response', 'index.vnd', 'inkml+xml',
                              'IOTP', 'ipfix', 'ipp', 'isup', 'its+xml',
                              'javascript', 'jf2feed+json', 'jose',
                              'jose+json', 'jrd+json', 'json',
                              'json-patch+json', 'json-seq', 'jwk+json',
                              'jwk-set+json', 'jwt', 'kpml-request+xml',
                              'kpml-response+xml', 'ld+json', 'lgr+xml',
                              'link-format', 'load-control+xml', 'lost+xml',
                              'lostsync+xml', 'LXF', 'mac-binhex40',
                              'macwriteii', 'mads+xml', 'marc', 'marcxml+xml',
                              'mathematica', 'mathml-content+xml',
                              'mathml-presentation+xml', 'mathml+xml',
                              'mbms-associated-procedure-description+xml',
                              'mbms-deregister+xml', 'mbms-envelope+xml',
                              'mbms-msk-response+xml', 'mbms-msk+xml',
                              'mbms-protection-description+xml',
                             'mbms-reception-report+xml',
                             'mbms-register-response+xml', 'mbms-register+xml',
                             'mbms-schedule+xml',
                             'mbms-user-service-description+xml', 'mbox',
                             'media_control+xml', 'media-policy-dataset+xml',
                             'mediaservercontrol+xml', 'merge-patch+json',
                             'metalink4+xml', 'mets+xml', 'MF4', 'mikey',
                             'mipc', 'mmt-aei+xml', 'mmt-usd+xml', 'mods+xml',
                             'moss-keys', 'moss-signature', 'mosskey-data',
                             'mosskey-request', 'mp21', 'mp4', 'mpeg4-generic',
                             'mpeg4-iod', 'mpeg4-iod-xmt', 'mrb-consumer+xml',
                             'mrb-publish+xml', 'msc-ivr+xml', 'msc-mixer+xml',
                             'msword', 'mud+json', 'mxf', 'n-quads',
                             'n-triples', 'nasdata', 'news-checkgroups',
                             'news-groupinfo', 'news-transmission',
                             'nlsml+xml', 'node', 'nss', 'ocsp-request',
                             'ocsp-response', 'octet-stream', 'ODA', 'odm+xml',
                             'ODX', 'oebps-package+xml', 'ogg', 'oscore',
                             'oxps', 'p2p-overlay+xml', 'parityfec',
                             'passport', 'patch-ops-error+xml', 'pdf', 'PDX',
                             'pem-certificate-chain', 'pgp-encrypted',
                             'pgp-keys', 'pgp-signature', 'pidf-diff+xml',
                             'pidf+xml', 'pkcs10', 'pkcs7-mime',
                             'pkcs7-signature', 'pkcs8', 'pkcs8-encrypted',
                             'pkcs12', 'pkix-attr-cert', 'pkix-cert',
                             'pkix-crl', 'pkix-pkipath', 'pkixcmp', 'pls+xml',
                             'poc-settings+xml', 'postscript',
                             'ppsp-tracker+json', 'problem+json',
                             'problem+xml', 'provenance+xml',
                             'prs.alvestrand.titrax-sheet', 'prs.cww',
                             'prs.hpub+zip', 'prs.nprend', 'prs.plucker',
                             'prs.rdf-xml-crypt', 'prs.xsf+xml', 'pskc+xml',
                             'rdf+xml', 'route-apd+xml', 'route-s-tsid+xml',
                             'route-usd+xml', 'QSIG', 'raptorfec', 'rdap+json',
                             'reginfo+xml', 'relax-ng-compact-syntax',
                             'remote-printing', 'reputon+json',
                             'resource-lists-diff+xml', 'resource-lists+xml',
                             'rfc+xml', 'riscos', 'rlmi+xml',
                             'rls-services+xml', 'rpki-ghostbusters',
                             'rpki-manifest', 'rpki-publication', 'rpki-roa',
                             'rpki-updown', 'rtf', 'rtploopback', 'rtx',
                             'samlassertion+xml', 'samlmetadata+xml',
                             'sbml+xml', 'scaip+xml', 'scim+json',
                             'scvp-cv-request', 'scvp-cv-response',
                             'scvp-vp-request', 'scvp-vp-response', 'sdp',
                             'secevent+jwt', 'senml-exi', 'senml+cbor',
                             'senml+json', 'senml+xml', 'sensml-exi',
                             'sensml+cbor', 'sensml+json', 'sensml+xml',
                             'sep-exi', 'sep+xml', 'session-info',
                             'set-payment', 'set-payment-initiation',
                             'set-registration', 'set-registration-initiation',
                             'sgml', 'sgml-open-catalog', 'shf+xml', 'sieve',
                             'simple-filter+xml', 'simple-message-summary',
                             'simpleSymbolContainer', 'sipc', 'slate',
                             'smil+xml', 'smpte336m', 'soap+fastinfoset',
                             'soap+xml', 'sparql-query', 'sparql-results+xml',
                             'spirits-event+xml', 'sql', 'srgs', 'srgs+xml',
                             'sru+xml', 'ssml+xml', 'stix+json', 'swid+xml',
                             'tamp-apex-update', 'tamp-apex-update-confirm',
                             'tamp-community-update',
                             'tamp-community-update-confirm', 'tamp-error',
                             'tamp-sequence-adjust',
                             'tamp-sequence-adjust-confirm',
                             'tamp-status-query', 'tamp-status-response',
                             'tamp-update', 'tamp-update-confirm',
                             'taxii+json', 'tei+xml', 'TETRA_ISI',
                             'thraud+xml', 'timestamp-query',
                             'timestamp-reply', 'timestamped-data',
                             'tlsrpt+gzip', 'tlsrpt+json', 'tnauthlist',
                             'trickle-ice-sdpfrag', 'trig', 'ttml+xml',
                             'tve-trigger', 'tzif', 'tzif-leap', 'ulpfec',
                             'urc-grpsheet+xml', 'urc-ressheet+xml',
                             'urc-targetdesc+xml', 'urc-uisocketdesc+xml',
                             'vcard+json', 'vcard+xml', 'vemmi',
                             'vnd.1000minds.decision-model+xml',
                             'vnd.3gpp.access-transfer-events+xml',
                             'vnd.3gpp.bsf+xml', 'vnd.3gpp.GMOP+xml',
                             'vnd.3gpp.mc-signalling-ear',
                             'vnd.3gpp.mcdata-affiliation-command+xml',
                             'vnd.3gpp.mcdata-info+xml',
                             'vnd.3gpp.mcdata-payload',
                             'vnd.3gpp.mcdata-service-config+xml',
                             'vnd.3gpp.mcdata-signalling',
                             'vnd.3gpp.mcdata-ue-config+xml',
                             'vnd.3gpp.mcdata-user-profile+xml',
                             'vnd.3gpp.mcptt-affiliation-command+xml',
                             'vnd.3gpp.mcptt-floor-request+xml',
                             'vnd.3gpp.mcptt-info+xml',
                             'vnd.3gpp.mcptt-location-info+xml',
                             'vnd.3gpp.mcptt-mbms-usage-info+xml',
                             'vnd.3gpp.mcptt-service-config+xml',
                             'vnd.3gpp.mcptt-signed+xml',
                             'vnd.3gpp.mcptt-ue-config+xml',
                             'vnd.3gpp.mcptt-ue-init-config+xml',
                             'vnd.3gpp.mcptt-user-profile+xml',
                             'vnd.3gpp.mcvideo-affiliation-command+xml',
                             'vnd.3gpp.mcvideo-info+xml',
                             'vnd.3gpp.mcvideo-location-info+xml',
                             'vnd.3gpp.mcvideo-mbms-usage-info+xml',
                             'vnd.3gpp.mcvideo-service-config+xml',
                             'vnd.3gpp.mcvideo-transmission-request+xml',
                             'vnd.3gpp.mcvideo-ue-config+xml',
                             'vnd.3gpp.mcvideo-user-profile+xml',
                             'vnd.3gpp.mid-call+xml', 'vnd.3gpp.pic-bw-large',
                             'vnd.3gpp.pic-bw-small', 'vnd.3gpp.pic-bw-var',
                             'vnd.3gpp-prose-pc3ch+xml', 'vnd.3gpp-prose+xml',
                             'vnd.3gpp.sms', 'vnd.3gpp.sms+xml',
                             'vnd.3gpp.srvcc-ext+xml',
                             'vnd.3gpp.SRVCC-info+xml',
                             'vnd.3gpp.state-and-event-info+xml',
                             'vnd.3gpp.ussd+xml',
                             'vnd.3gpp-v2x-local-service-information',
                             'vnd.3gpp2.bcmcsinfo+xml', 'vnd.3gpp2.sms',
                             'vnd.3gpp2.tcap', 'vnd.3lightssoftware.imagescal',
                             'vnd.3M.Post-it-Notes', 'vnd.accpac.simply.aso',
                             'vnd.accpac.simply.imp', 'vnd.acucobol',
                             'vnd.acucorp', 'vnd.adobe.flash.movie',
                             'vnd.adobe.formscentral.fcdt', 'vnd.adobe.fxp',
                             'vnd.adobe.partial-upload', 'vnd.adobe.xdp+xml',
                             'vnd.adobe.xfdf', 'vnd.aether.imp',
                             'vnd.afpc.afplinedata', 'vnd.afpc.modca',
                             'vnd.ah-barcode', 'vnd.ahead.space',
                             'vnd.airzip.filesecure.azf',
                             'vnd.airzip.filesecure.azs', 'vnd.amadeus+json',
                             'vnd.amazon.mobi8-ebook',
                             'vnd.americandynamics.acc', 'vnd.amiga.ami',
                             'vnd.amundsen.maze+xml', 'vnd.android.ota',
                             'vnd.anki',
                             'vnd.anser-web-certificate-issue-initiation',
                             'vnd.antix.game-component',
                             'vnd.apache.thrift.binary',
                             'vnd.apache.thrift.compact',
                             'vnd.apache.thrift.json', 'vnd.api+json',
                             'vnd.apothekende.reservation+json',
                             'vnd.apple.installer+xml', 'vnd.apple.keynote',
                             'vnd.apple.mpegurl', 'vnd.apple.numbers',
                             'vnd.apple.pages', 'vnd.aristanetworks.swi',
                             'vnd.artisan+json', 'vnd.artsquare',
                             'vnd.astraea-software.iota', 'vnd.audiograph',
                             'vnd.autopackage', 'vnd.avalon+json',
                             'vnd.avistar+xml', 'vnd.balsamiq.bmml+xml',
                             'vnd.banana-accounting', 'vnd.bbf.usp.error',
                             'vnd.bbf.usp.msg', 'vnd.bbf.usp.msg+json',
                             'vnd.balsamiq.bmpr', 'vnd.bekitzur-stech+json',
                             'vnd.bint.med-content', 'vnd.biopax.rdf+xml',
                             'vnd.blink-idb-value-wrapper',
                             'vnd.blueice.multipass', 'vnd.bluetooth.ep.oob',
                             'vnd.bluetooth.le.oob', 'vnd.bmi', 'vnd.bpf',
                             'vnd.bpf3', 'vnd.businessobjects',
                             'vnd.byu.uapi+json', 'vnd.cab-jscript',
                             'vnd.canon-cpdl', 'vnd.canon-lips',
                             'vnd.capasystems-pg+json',
                             'vnd.cendio.thinlinc.clientconf',
                             'vnd.century-systems.tcp_stream',
                             'vnd.chemdraw+xml', 'vnd.chess-pgn',
                             'vnd.chipnuts.karaoke-mmd', 'vnd.ciedi',
                             'vnd.cinderella', 'vnd.cirpack.isdn-ext',
                             'vnd.citationstyles.style+xml', 'vnd.claymore',
                             'vnd.cloanto.rp9', 'vnd.clonk.c4group',
                             'vnd.cluetrust.cartomobile-config',
                             'vnd.cluetrust.cartomobile-config-pkg',
                             'vnd.coffeescript',
                             'vnd.collabio.xodocuments.document',
                             'vnd.collabio.xodocuments.document-template',
                             'vnd.collabio.xodocuments.presentation',
                             'vnd.collabio.xodocuments.presentation-template',
                             'vnd.collabio.xodocuments.spreadsheet',
                             'vnd.collabio.xodocuments.spreadsheet-template',
                             'vnd.collection.doc+json', 'vnd.collection+json',
                             'vnd.collection.next+json', 'vnd.comicbook-rar',
                             'vnd.comicbook+zip', 'vnd.commerce-battelle',
                             'vnd.commonspace', 'vnd.coreos.ignition+json',
                             'vnd.cosmocaller', 'vnd.contact.cmsg',
                             'vnd.crick.clicker', 'vnd.crick.clicker.keyboard',
                             'vnd.crick.clicker.palette',
                             'vnd.crick.clicker.template',
                             'vnd.crick.clicker.wordbank',
                             'vnd.criticaltools.wbs+xml',
                             'vnd.cryptii.pipe+json', 'vnd.crypto-shade-file',
                             'vnd.ctc-posml', 'vnd.ctct.ws+xml',
                             'vnd.cups-pdf', 'vnd.cups-postscript',
                             'vnd.cups-ppd', 'vnd.cups-raster', 'vnd.cups-raw',
                             'vnd.curl', 'vnd.cyan.dean.root+xml',
                             'vnd.cybank', 'vnd.d2l.coursepackage1p0+zip',
                             'vnd.dart', 'vnd.data-vision.rdz',
                             'vnd.datapackage+json', 'vnd.dataresource+json',
                             'vnd.debian.binary-package', 'vnd.dece.data',
                             'vnd.dece.ttml+xml', 'vnd.dece.unspecified',
                             'vnd.dece.zip', 'vnd.denovo.fcselayout-link',
                             'vnd.desmume.movie',
                             'vnd.dir-bi.plate-dl-nosuffix',
                             'vnd.dm.delegation+xml', 'vnd.dna',
                             'vnd.document+json', 'vnd.dolby.mobile.1',
                             'vnd.dolby.mobile.2',
                             'vnd.doremir.scorecloud-binary-document',
                             'vnd.dpgraph', 'vnd.dreamfactory',
                             'vnd.drive+json', 'vnd.dtg.local',
                             'vnd.dtg.local.flash', 'vnd.dtg.local.html',
                             'vnd.dvb.ait', 'vnd.dvb.dvbj',
                             'vnd.dvb.esgcontainer',
                             'vnd.dvb.ipdcdftnotifaccess',
                             'vnd.dvb.ipdcesgaccess', 'vnd.dvb.ipdcesgaccess2',
                             'vnd.dvb.ipdcesgpdd', 'vnd.dvb.ipdcroaming',
                             'vnd.dvb.iptv.alfec-base',
                             'vnd.dvb.iptv.alfec-enhancement', 
                             'vnd.dvb.notif-aggregate-root+xml',
                             'vnd.dvb.notif-container+xml',
                             'vnd.dvb.notif-generic+xml',
                             'vnd.dvb.notif-ia-msglist+xml',
                             'vnd.dvb.notif-ia-registration-request+xml',
                             'vnd.dvb.notif-ia-registration-response+xml', 
                             'vnd.dvb.notif-init+xml', 'vnd.dvb.pfr',
                             'vnd.dvb.service', 'vnd.dxr', 'vnd.dynageo',
                             'vnd.dzr', 'vnd.easykaraoke.cdgdownload',
                             'vnd.ecip.rlp', 'vnd.ecdis-update',
                             'vnd.ecowin.chart', 'vnd.ecowin.filerequest',
                             'vnd.ecowin.fileupdate', 'vnd.ecowin.series',
                             'vnd.ecowin.seriesrequest',
                             'vnd.ecowin.seriesupdate', 'vnd.efi.img',
                             'vnd.efi.iso', 'vnd.emclient.accessrequest+xml',
                             'vnd.enliven', 'vnd.enphase.envoy',
                             'vnd.eprints.data+xml', 'vnd.epson.esf',
                             'vnd.epson.msf', 'vnd.epson.quickanime',
                             'vnd.epson.salt', 'vnd.epson.ssf',
                             'vnd.ericsson.quickcall', 'vnd.espass-espass+zip',
                             'vnd.eszigno3+xml', 'vnd.etsi.aoc+xml',
                             'vnd.etsi.asic-s+zip', 'vnd.etsi.asic-e+zip',
                             'vnd.etsi.cug+xml', 'vnd.etsi.iptvcommand+xml',
                             'vnd.etsi.iptvdiscovery+xml',
                             'vnd.etsi.iptvprofile+xml',
                             'vnd.etsi.iptvsad-bc+xml',
                             'vnd.etsi.iptvsad-cod+xml',
                             'vnd.etsi.iptvsad-npvr+xml',
                             'vnd.etsi.iptvservice+xml',
                             'vnd.etsi.iptvsync+xml'
                             'vnd.etsi.iptvueprofile+xml', 'vnd.etsi.mcid+xml',
                             'vnd.etsi.mheg5',
                             'vnd.etsi.overload-control-policy-dataset+xml',
                             'vnd.etsi.pstn+xml', 'vnd.etsi.sci+xml',
                             'vnd.etsi.simservs+xml',
                             'vnd.etsi.timestamp-token',
                             'vnd.etsi.tsl+xml', 'vnd.etsi.tsl.der',
                             'vnd.evolv.ecig.profile',
                             'vnd.evolv.ecig.settings', 'vnd.evolv.ecig.theme',
                             'vnd.eudora.data', 'vnd.exstream-empower+zip',
                             'vnd.exstream-package', 'vnd.ezpix-album',
                             'vnd.ezpix-package', 'vnd.f-secure.mobile',
                             'vnd.fastcopy-disk-image', 'vnd.fdf',
                             'vnd.fdsn.mseed', 'vnd.fdsn.seed',
                             'vnd.ffsns', 'vnd.filmit.zfc', 'vnd.fints',
                             'vnd.firemonkeys.cloudcell', 'vnd.FloGraphIt',
                             'vnd.fluxtime.clip', 'vnd.font-fontforge-sfd',
                             'vnd.framemaker', 'vnd.frogans.fnc',
                             'vnd.frogans.ltf', 'vnd.fsc.weblaunch',
                             'vnd.fujitsu.oasys', 'vnd.fujitsu.oasys2',
                             'vnd.fujitsu.oasys3', 'vnd.fujitsu.oasysgp',
                             'vnd.fujitsu.oasysprs', 'vnd.fujixerox.ART4',
                             'vnd.fujixerox.ART-EX', 'vnd.fujixerox.ddd',
                             'vnd.fujixerox.docuworks',
                             'vnd.fujixerox.docuworks.binder',
                             'vnd.fujixerox.docuworks.container',
                             'vnd.fujixerox.HBPL', 'vnd.fut-misnet',
                             'vnd.futoin+cbor', 'vnd.futoin+json',
                             'vnd.fuzzysheet', 'vnd.genomatix.tuxedo',
                             'vnd.geogebra.file', 'vnd.geogebra.tool',
                             'vnd.geometry-explorer', 'vnd.geonext',
                             'vnd.geoplan', 'vnd.geospace', 'vnd.gerber',
                             'vnd.globalplatform.card-content-mgt',
                             'vnd.globalplatform.card-content-mgt-response',
                             'vnd.gmx - DEPRECATED','vnd.google-earth.kml+xml',
                             'vnd.google-earth.kmz', 'vnd.gov.sk.e-form+xml',
                             'vnd.gov.sk.e-form+zip',
                             'vnd.gov.sk.xmldatacontainer+xml', 'vnd.grafeq',
                             'vnd.gridmp', 'vnd.groove-account',
                             'vnd.groove-help', 'vnd.groove-identity-message',
                             'vnd.groove-injector', 'vnd.groove-tool-message',
                             'vnd.groove-tool-template', 'vnd.groove-vcard',
                             'vnd.hal+json', 'vnd.hal+xml',
                             'vnd.HandHeld-Entertainment+xml', 'vnd.hbci',
                             'vnd.hc+json', 'vnd.hcl-bireports', 'vnd.hdt',
                             'vnd.heroku+json', 'vnd.hhe.lesson-player',
                             'vnd.hp-HPGL', 'vnd.hp-hpid', 'vnd.hp-hps',
                             'vnd.hp-jlyt', 'vnd.hp-PCL', 'vnd.hp-PCLXL',
                             'vnd.httphone', 'vnd.hydrostatix.sof-data',
                             'vnd.hyper-item+json', 'vnd.hyper+json',
                             'vnd.hyperdrive+json', 'vnd.hzn-3d-crossword',
                             'vnd.ibm.electronic-media', 'vnd.ibm.MiniPay',
                             'vnd.ibm.rights-management',
                             'vnd.ibm.secure-container', 'vnd.iccprofile',
                             'vnd.ieee.1905', 'vnd.igloader',
                             'vnd.imagemeter.folder+zip',
                             'vnd.imagemeter.image+zip', 'vnd.immervision-ivp',
                             'vnd.immervision-ivu', 'vnd.ims.imsccv1p1',
                             'vnd.ims.imsccv1p2', 'vnd.ims.imsccv1p3',
                             'vnd.ims.lis.v2.result+json',
                             'vnd.ims.lti.v2.toolconsumerprofile+json',
                             'vnd.ims.lti.v2.toolproxy.id+json',
                             'vnd.ims.lti.v2.toolproxy+json',
                             'vnd.ims.lti.v2.toolsettings+json',
                             'vnd.ims.lti.v2.toolsettings.simple+json',
                             'vnd.informedcontrol.rms+xml',
                             'vnd.infotech.project','vnd.infotech.project+xml',
                             'vnd.innopath.wamp.notification','vnd.insors.igm',
                             'vnd.intercon.formnet', 'vnd.intergeo',
                             'vnd.intertrust.digibox', 'vnd.intertrust.nncp',
                             'vnd.intu.qbo', 'vnd.intu.qfx',
                             'vnd.iptc.g2.catalogitem+xml',
                             'vnd.iptc.g2.conceptitem+xml',
                             'vnd.iptc.g2.knowledgeitem+xml',
                             'vnd.iptc.g2.newsitem+xml',
                             'vnd.iptc.g2.newsmessage+xml',
                             'vnd.iptc.g2.packageitem+xml',
                             'vnd.iptc.g2.planningitem+xml',
                             'vnd.ipunplugged.rcprofile',
                             'vnd.irepository.package+xml',
                             'vnd.is-xpr', 'vnd.isac.fcs', 'vnd.jam',
                             'vnd.iso11783-10+zip',
                             'vnd.japannet-directory-service',
                             'vnd.japannet-jpnstore-wakeup',
                             'vnd.japannet-payment-wakeup',
                             'vnd.japannet-registration',
                             'vnd.japannet-registration-wakeup',
                             'vnd.japannet-setstore-wakeup',
                             'vnd.japannet-verification',
                             'vnd.japannet-verification-wakeup',
                             'vnd.jcp.javame.midlet-rms', 'vnd.jisp',
                             'vnd.joost.joda-archive', 'vnd.jsk.isdn-ngn',
                             'vnd.kahootz', 'vnd.kde.karbon', 'vnd.kde.kchart',
                             'vnd.kde.kformula', 'vnd.kde.kivio',
                             'vnd.kde.kontour', 'vnd.kde.kpresenter',
                             'vnd.kde.kspread', 'vnd.kde.kword',
                             'vnd.kenameaapp', 'vnd.kidspiration', 'vnd.Kinar',
                             'vnd.koan', 'vnd.kodak-descriptor', 'vnd.las',
                             'vnd.las.las+json', 'vnd.las.las+xml',
                             'vnd.laszip', 'vnd.leap+json',
                             'vnd.liberty-request+xml',
                             'vnd.llamagraphics.life-balance.desktop',
                             'vnd.llamagraphics.life-balance.exchange+xml',
                             'vnd.logipipe.circuit+zip', 'vnd.loom',
                             'vnd.lotus-1-2-3', 'vnd.lotus-approach',
                             'vnd.lotus-freelance', 'vnd.lotus-notes',
                             'vnd.lotus-organizer', 'vnd.lotus-screencam',
                             'vnd.lotus-wordpro', 'vnd.macports.portpkg',
                             'vnd.mapbox-vector-tile',
                             'vnd.marlin.drm.actiontoken+xml',
                             'vnd.marlin.drm.conftoken+xml',
                             'vnd.marlin.drm.license+xml',
                             'vnd.marlin.drm.mdcf', 'vnd.mason+json',
                             'vnd.maxmind.maxmind-db', 'vnd.mcd',
                             'vnd.medcalcdata', 'vnd.mediastation.cdkey',
                             'vnd.meridian-slingshot', 'vnd.MFER', 'vnd.mfmp',
                             'vnd.micro+json', 'vnd.micrografx.flo',
                             'vnd.micrografx.igx',
                             'vnd.microsoft.portable-executable',
                             'vnd.microsoft.windows.thumbnail-cache',
                             'vnd.miele+json', 'vnd.mif',
                             'vnd.minisoft-hp3000-save',
                             'vnd.mitsubishi.misty-guard.trustweb',
                             'vnd.Mobius.DAF', 'vnd.Mobius.DIS',
                             'vnd.Mobius.MBK', 'vnd.Mobius.MQY',
                             'vnd.Mobius.MSL', 'vnd.Mobius.PLC',
                             'vnd.Mobius.TXF', 'vnd.mophun.application',
                             'vnd.mophun.certificate','vnd.motorola.flexsuite',
                             'vnd.motorola.flexsuite.adsi',
                             'vnd.motorola.flexsuite.fis',
                             'vnd.motorola.flexsuite.gotap',
                             'vnd.motorola.flexsuite.kmr',
                             'vnd.motorola.flexsuite.ttc',
                             'vnd.motorola.flexsuite.wem', 'vnd.motorola.iprm',
                             'vnd.mozilla.xul+xml', 'vnd.ms-artgalry',
                             'vnd.ms-asf', 'vnd.ms-cab-compressed',
                             'vnd.ms-3mfdocument', 'vnd.ms-excel',
                             'vnd.ms-excel.addin.macroEnabled.12',
                             'vnd.ms-excel.sheet.binary.macroEnabled.12',
                             'vnd.ms-excel.sheet.macroEnabled.12',
                             'vnd.ms-excel.template.macroEnabled.12',
                             'vnd.ms-fontobject', 'vnd.ms-htmlhelp',
                             'vnd.ms-ims', 'vnd.ms-lrm',
                             'vnd.ms-office.activeX+xml', 'vnd.ms-officetheme',
                             'vnd.ms-playready.initiator+xml',
                             'vnd.ms-powerpoint',
                             'vnd.ms-powerpoint.addin.macroEnabled.12',
                             'vnd.ms-powerpoint.presentation.macroEnabled.12',
                             'vnd.ms-powerpoint.slide.macroEnabled.12',
                             'vnd.ms-powerpoint.slideshow.macroEnabled.12',
                             'vnd.ms-powerpoint.template.macroEnabled.12',
                             'vnd.ms-PrintDeviceCapabilities+xml',
                             'vnd.ms-PrintSchemaTicket+xml', 'vnd.ms-project',
                             'vnd.ms-tnef', 'vnd.ms-windows.devicepairing',
                             'vnd.ms-windows.nwprinting.oob',
                             'vnd.ms-windows.printerpairing',
                             'vnd.ms-windows.wsd.oob',
                             'vnd.ms-wmdrm.lic-chlg-req',
                             'vnd.ms-wmdrm.lic-resp',
                             'vnd.ms-wmdrm.meter-chlg-req',
                             'vnd.ms-wmdrm.meter-resp',
                             'vnd.ms-word.document.macroEnabled.12',
                             'vnd.ms-word.template.macroEnabled.12',
                             'vnd.ms-works', 'vnd.ms-wpl',
                             'vnd.ms-xpsdocument', 'vnd.msa-disk-image',
                             'vnd.mseq', 'vnd.msign', 'vnd.multiad.creator',
                             'vnd.multiad.creator.cif', 'vnd.musician',
                             'vnd.music-niff', 'vnd.muvee.style', 'vnd.mynfc',
                             'vnd.ncd.control', 'vnd.ncd.reference',
                             'vnd.nearst.inv+json', 'vnd.nervana',
                             'vnd.netfpx', 'vnd.neurolanguage.nlu',
                             'vnd.nimn', 'vnd.nintendo.snes.rom',
                             'vnd.nintendo.nitro.rom', 'vnd.nitf',
                             'vnd.noblenet-directory', 'vnd.noblenet-sealer',
                             'vnd.noblenet-web', 'vnd.nokia.catalogs',
                             'vnd.nokia.conml+wbxml', 'vnd.nokia.conml+xml',
                             'vnd.nokia.iptv.config+xml',
                             'vnd.nokia.iSDS-radio-presets',
                             'vnd.nokia.landmark+wbxml',
                             'vnd.nokia.landmark+xml',
                             'vnd.nokia.landmarkcollection+xml',
                             'vnd.nokia.ncd', 'vnd.nokia.n-gage.ac+xml',
                             'vnd.nokia.n-gage.data',
                             'vnd.nokia.pcd+wbxml', 'vnd.nokia.pcd+xml',
                             'vnd.nokia.radio-preset',
                             'vnd.nokia.radio-presets', 'vnd.novadigm.EDM',
                             'vnd.novadigm.EDX', 'vnd.novadigm.EXT',
                             'vnd.ntt-local.content-share',
                             'vnd.ntt-local.file-transfer',
                             'vnd.ntt-local.ogw_remote-access',
                             'vnd.ntt-local.sip-ta_remote',
                             'vnd.ntt-local.sip-ta_tcp_stream',
                             'vnd.oasis.opendocument.chart',
                             'vnd.oasis.opendocument.chart-template',
                             'vnd.oasis.opendocument.database',
                             'vnd.oasis.opendocument.formula',
                             'vnd.oasis.opendocument.formula-template',
                             'vnd.oasis.opendocument.graphics',
                             'vnd.oasis.opendocument.graphics-template',
                             'vnd.oasis.opendocument.image',
                             'vnd.oasis.opendocument.image-template',
                             'vnd.oasis.opendocument.presentation',
                             'vnd.oasis.opendocument.presentation-template',
                             'vnd.oasis.opendocument.spreadsheet',
                             'vnd.oasis.opendocument.spreadsheet-template',
                             'vnd.oasis.opendocument.text',
                             'vnd.oasis.opendocument.text-master',
                             'vnd.oasis.opendocument.text-template',
                             'vnd.oasis.opendocument.text-web', 'vnd.obn',
                             'vnd.ocf+cbor', 'vnd.oftn.l10n+json',
                             'vnd.oipf.contentaccessdownload+xml',
                             'vnd.oipf.contentaccessstreaming+xml',
                             'vnd.oipf.cspg-hexbinary', 'vnd.oipf.dae.svg+xml',
                             'vnd.oipf.dae.xhtml+xml',
                             'vnd.oipf.mippvcontrolmessage+xml',
                             'vnd.oipf.pae.gem', 'vnd.oipf.spdiscovery+xml',
                             'vnd.oipf.spdlist+xml', 'vnd.oipf.ueprofile+xml',
                             'vnd.oipf.userprofile+xml', 'vnd.olpc-sugar',
                             'vnd.oma.bcast.associated-procedure-parameter+xml',
                             'vnd.oma.bcast.drm-trigger+xml',
                             'vnd.oma.bcast.imd+xml', 'vnd.oma.bcast.ltkm',
                             'vnd.oma.bcast.notification+xml',
                             'vnd.oma.bcast.provisioningtrigger',
                             'vnd.oma.bcast.sgboot', 'vnd.oma.bcast.sgdd+xml',
                             'vnd.oma.bcast.sgdu',
                             'vnd.oma.bcast.simple-symbol-container',
                             'vnd.oma.bcast.smartcard-trigger+xml',
                             'vnd.oma.bcast.sprov+xml', 'vnd.oma.bcast.stkm',
                             'vnd.oma.cab-address-book+xml',
                             'vnd.oma.cab-feature-handler+xml',
                             'vnd.oma.cab-pcc+xml',
                             'vnd.oma.cab-subs-invite+xml',
                             'vnd.oma.cab-user-prefs+xml', 'vnd.oma.dcd',
                             'vnd.oma.dcdc', 'vnd.oma.dd2+xml',
                             'vnd.oma.drm.risd+xml',
                             'vnd.oma.group-usage-list+xml',
                             'vnd.oma.lwm2m+json', 'vnd.oma.lwm2m+tlv',
                             'vnd.oma.pal+xml',
                             'vnd.oma.poc.detailed-progress-report+xml',
                             'vnd.oma.poc.final-report+xml',
                             'vnd.oma.poc.groups+xml',
                             'vnd.oma.poc.invocation-descriptor+xml',
                             'vnd.oma.poc.optimized-progress-report+xml',
                             'vnd.oma.push', 'vnd.oma.scidm.messages+xml',
                             'vnd.oma.xcap-directory+xml',
                             'vnd.omads-email+xml', 'vnd.omads-file+xml',
                             'vnd.omads-folder+xml', 'vnd.omaloc-supl-init',
                             'vnd.oma-scws-config',
                             'vnd.oma-scws-http-request',
                             'vnd.oma-scws-http-response', 'vnd.onepager',
                             'vnd.onepagertamp', 'vnd.onepagertamx',
                             'vnd.onepagertat', 'vnd.onepagertatp',
                             'vnd.onepagertatx', 'vnd.openblox.game-binary',
                             'vnd.openblox.game+xml', 'vnd.openeye.oeb',
                             'vnd.openstreetmap.data+xml',
                             'vnd.openxmlformats-officedocument.custom-properties+xml',
                             'vnd.openxmlformats-officedocument.customXmlProperties+xml',
                             'vnd.openxmlformats-officedocument.drawing+xml',
                             'vnd.openxmlformats-officedocument.drawingml.chart+xml',
                             'vnd.openxmlformats-officedocument.drawingml.chartshapes+xml',
                             'vnd.openxmlformats-officedocument.drawingml.diagramColors+xml',
                             'vnd.openxmlformats-officedocument.drawingml.diagramData+xml',
                             'vnd.openxmlformats-officedocument.drawingml.diagramLayout+xml',
                             'vnd.openxmlformats-officedocument.drawingml.diagramStyle+xml',
                             'vnd.openxmlformats-officedocument.extended-properties+xml',
                             'vnd.openxmlformats-officedocument.presentationml.commentAuthors+xml',
                             'vnd.openxmlformats-officedocument.presentationml.comments+xml',
                             'vnd.openxmlformats-officedocument.presentationml.handoutMaster+xml',
                             'vnd.openxmlformats-officedocument.presentationml.notesMaster+xml',
                             'vnd.openxmlformats-officedocument.presentationml.notesSlide+xml',
                             'vnd.openxmlformats-officedocument.presentationml.presentation',
                             'vnd.openxmlformats-officedocument.presentationml.presentation.main+xml',
                             'vnd.openxmlformats-officedocument.presentationml.presProps+xml',
                             'vnd.openxmlformats-officedocument.presentationml.slide',
                             'vnd.openxmlformats-officedocument.presentationml.slide+xml',
                             'vnd.openxmlformats-officedocument.presentationml.slideLayout+xml',
                             'vnd.openxmlformats-officedocument.presentationml.slideMaster+xml',
                             'vnd.openxmlformats-officedocument.presentationml.slideshow',
                             'vnd.openxmlformats-officedocument.presentationml.slideshow.main+xml',
                             'vnd.openxmlformats-officedocument.presentationml.slideUpdateInfo+xml',
                             'vnd.openxmlformats-officedocument.presentationml.tableStyles+xml',
                             'vnd.openxmlformats-officedocument.presentationml.tags+xml',
                             'vnd.openxmlformats-officedocument.presentationml.template',
                             'vnd.openxmlformats-officedocument.presentationml.template.main+xml',
                             'vnd.openxmlformats-officedocument.presentationml.viewProps+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.calcChain+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.chartsheet+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.comments+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.connections+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.dialogsheet+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.externalLink+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheDefinition+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheRecords+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.pivotTable+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.queryTable+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.revisionHeaders+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.revisionLog+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                             'vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.sheetMetadata+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.styles+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.table+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.tableSingleCells+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.template',
                             'vnd.openxmlformats-officedocument.spreadsheetml.template.main+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.userNames+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.volatileDependencies+xml',
                             'vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml',
                             'vnd.openxmlformats-officedocument.theme+xml',
                             'vnd.openxmlformats-officedocument.themeOverride+xml',
                             'vnd.openxmlformats-officedocument.vmlDrawing',
                             'vnd.openxmlformats-officedocument.wordprocessingml.comments+xml',
                             'vnd.openxmlformats-officedocument.wordprocessingml.document',
                             'vnd.openxmlformats-officedocument.wordprocessingml.document.glossary+xml',
                             'vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml',
                             'vnd.openxmlformats-officedocument.wordprocessingml.endnotes+xml',
                             'vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml',
                             'vnd.openxmlformats-officedocument.wordprocessingml.footer+xml',
                             'vnd.openxmlformats-officedocument.wordprocessingml.footnotes+xml',
                             'vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml',
                             'vnd.openxmlformats-officedocument.wordprocessingml.settings+xml',
                             'vnd.openxmlformats-officedocument.wordprocessingml.styles+xml',
                             'vnd.openxmlformats-officedocument.wordprocessingml.template',
                             'vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml',
                             'vnd.openxmlformats-officedocument.wordprocessingml.webSettings+xml',
                             'vnd.openxmlformats-package.core-properties+xml',
                             'vnd.openxmlformats-package.digital-signature-xmlsignature+xml',
                             'vnd.openxmlformats-package.relationships+xml',
                             'vnd.oracle.resource+json', 'vnd.orange.indata',
                             'vnd.osa.netdeploy', 'vnd.osgeo.mapguide.package',
                             'vnd.osgi.bundle', 'vnd.osgi.dp',
                             'vnd.osgi.subsystem', 'vnd.otps.ct-kip+xml',
                             'vnd.oxli.countgraph', 'vnd.pagerduty+json',
                             'vnd.palm', 'vnd.panoply', 'vnd.paos.xml',
                             'vnd.patentdive', 'vnd.patientecommsdoc',
                             'vnd.pawaafile', 'vnd.pcos', 'vnd.pg.format',
                             'vnd.pg.osasli',
                             'vnd.piaccess.application-licence', 'vnd.picsel',
                             'vnd.pmi.widget',
                             'vnd.poc.group-advertisement+xml',
                             'vnd.pocketlearn', 'vnd.powerbuilder6',
                             'vnd.powerbuilder6-s', 'vnd.powerbuilder7',
                             'vnd.powerbuilder75', 'vnd.powerbuilder75-s',
                             'vnd.powerbuilder7-s', 'vnd.preminet',
                             'vnd.previewsystems.box', 'vnd.proteus.magazine',
                             'vnd.psfs', 'vnd.publishare-delta-tree',
                             'vnd.pvi.ptid1', 'vnd.pwg-multiplexed',
                             'vnd.pwg-xhtml-print+xml',
                             'vnd.qualcomm.brew-app-res', 'vnd.quarantainenet',
                             'vnd.Quark.QuarkXPress',
                             'vnd.quobject-quoxdocument',
                             'vnd.radisys.moml+xml',
                             'vnd.radisys.msml-audit-conf+xml',
                             'vnd.radisys.msml-audit-conn+xml',
                             'vnd.radisys.msml-audit-dialog+xml',
                             'vnd.radisys.msml-audit-stream+xml',
                             'vnd.radisys.msml-audit+xml',
                             'vnd.radisys.msml-conf+xml',
                             'vnd.radisys.msml-dialog-base+xml',
                             'vnd.radisys.msml-dialog-fax-detect+xml',
                             'vnd.radisys.msml-dialog-fax-sendrecv+xml',
                             'vnd.radisys.msml-dialog-group+xml',
                             'vnd.radisys.msml-dialog-speech+xml',
                             'vnd.radisys.msml-dialog-transform+xml',
                             'vnd.radisys.msml-dialog+xml',
                             'vnd.radisys.msml+xml', 'vnd.rainstor.data',
                             'vnd.rapid', 'vnd.rar', 'vnd.realvnc.bed',
                             'vnd.recordare.musicxml',
                             'vnd.recordare.musicxml+xml',
                             'vnd.RenLearn.rlprint', 'vnd.restful+json',
                             'vnd.rig.cryptonote', 'vnd.route66.link66+xml',
                             'vnd.rs-274x', 'vnd.ruckus.download', 'vnd.s3sms',
                             'vnd.sailingtracker.track', 'vnd.sbm.cid',
                             'vnd.sbm.mid2', 'vnd.scribus', 'vnd.sealed.3df',
                             'vnd.sealed.csf', 'vnd.sealed.doc',
                             'vnd.sealed.eml', 'vnd.sealed.mht',
                             'vnd.sealed.net', 'vnd.sealed.ppt',
                             'vnd.sealed.tiff', 'vnd.sealed.xls',
                             'vnd.sealedmedia.softseal.html',
                             'vnd.sealedmedia.softseal.pdf', 'vnd.seemail',
                             'vnd.sema', 'vnd.semd', 'vnd.semf',
                             'vnd.shade-save-file',
                             'vnd.shana.informed.formdata',
                             'vnd.shana.informed.formtemplate',
                             'vnd.shana.informed.interchange',
                             'vnd.shana.informed.package',
                             'vnd.shootproof+json', 'vnd.shopkick+json',
                             'vnd.sigrok.session', 'vnd.SimTech-MindMapper',
                             'vnd.siren+json', 'vnd.smaf',
                             'vnd.smart.notebook', 'vnd.smart.teacher',
                             'vnd.software602.filler.form+xml',
                             'vnd.software602.filler.form-xml-zip',
                             'vnd.solent.sdkm+xml', 'vnd.spotfire.dxp',
                             'vnd.spotfire.sfs', 'vnd.sqlite3', 'vnd.sss-cod',
                             'vnd.sss-dtf', 'vnd.sss-ntf', 
                             'vnd.stepmania.package','vnd.stepmania.stepchart',
                             'vnd.street-stream', 'vnd.sun.wadl+xml',
                             'vnd.sus-calendar', 'vnd.svd','vnd.swiftview-ics',
                             'vnd.syncml.dm.notification',
                             'vnd.syncml.dmddf+xml', 'vnd.syncml.dmtnds+wbxml',
                             'vnd.syncml.dmtnds+xml', 'vnd.syncml.dmddf+wbxml',
                             'vnd.syncml.dm+wbxml', 'vnd.syncml.dm+xml',
                             'vnd.syncml.ds.notification', 'vnd.syncml+xml',
                             'vnd.tableschema+json',
                             'vnd.tao.intent-module-archive',
                             'vnd.tcpdump.pcap', 'vnd.think-cell.ppttc+json',
                             'vnd.tml', 'vnd.tmd.mediaflex.api+xml',
                             'vnd.tmobile-livetv', 'vnd.tri.onesource',
                             'vnd.trid.tpt', 'vnd.triscape.mxs',
                             'vnd.trueapp', 'vnd.truedoc',
                             'vnd.ubisoft.webplayer', 'vnd.ufdl',
                             'vnd.uiq.theme', 'vnd.umajin', 'vnd.unity',
                             'vnd.uoml+xml', 'vnd.uplanet.alert',
                             'vnd.uplanet.alert-wbxml',
                             'vnd.uplanet.bearer-choice',
                             'vnd.uplanet.bearer-choice-wbxml',
                             'vnd.uplanet.cacheop','vnd.uplanet.cacheop-wbxml',
                             'vnd.uplanet.channel','vnd.uplanet.channel-wbxml',
                             'vnd.uplanet.list', 'vnd.uplanet.listcmd',
                             'vnd.uplanet.listcmd-wbxml',
                             'vnd.uplanet.list-wbxml', 'vnd.uri-map',
                             'vnd.uplanet.signal', 'vnd.valve.source.material',
                             'vnd.vcx', 'vnd.vd-study', 'vnd.vectorworks',
                             'vnd.vel+json', 'vnd.verimatrix.vcas',
                             'vnd.veryant.thin', 'vnd.ves.encrypted',
                             'vnd.vidsoft.vidconference','vnd.visio',
                             'vnd.visionary', 'vnd.vividence.scriptfile',
                             'vnd.vsf', 'vnd.wap.sic', 'vnd.wap.slc',
                             'vnd.wap.wbxml', 'vnd.wap.wmlc',
                             'vnd.wap.wmlscriptc', 'vnd.webturbo',
                             'vnd.wfa.p2p', 'vnd.wfa.wsc',
                             'vnd.windows.devicepairing', 'vnd.wmc',
                             'vnd.wmf.bootstrap', 'vnd.wolfram.mathematica',
                             'vnd.wolfram.mathematica.package',
                             'vnd.wolfram.player', 'vnd.wordperfect',
                             'vnd.wqd', 'vnd.wrq-hp3000-labelled',
                             'vnd.wt.stf', 'vnd.wv.csp+xml',
                             'vnd.wv.csp+wbxml', 'vnd.wv.ssp+xml',
                             'vnd.xacml+json', 'vnd.xara', 'vnd.xfdl',
                             'vnd.xfdl.webform', 'vnd.xmi+xml',
                             'vnd.xmpie.cpkg', 'vnd.xmpie.dpkg',
                             'vnd.xmpie.plan', 'vnd.xmpie.ppkg',
                             'vnd.xmpie.xlim', 'vnd.yamaha.hv-dic',
                             'vnd.yamaha.hv-script', 'vnd.yamaha.hv-voice',
                             'vnd.yamaha.openscoreformat.osfpvg+xml',
                             'vnd.yamaha.openscoreformat',
                             'vnd.yamaha.remote-setup',
                             'vnd.yamaha.smaf-audio', 'vnd.yamaha.smaf-phrase',
                             'vnd.yamaha.through-ngn',
                             'vnd.yamaha.tunnel-udpencap', 'vnd.yaoweme',
                             'vnd.yellowriver-custom-menu',
                             'vnd.zul', 'vnd.zzazz.deck+xml', 'voicexml+xml',
                             'voucher-cms+json', 'vq-rtcpxr','watcherinfo+xml',
                             'webpush-options+json', 'whoispp-query',
                             'whoispp-response', 'widget', 'wita',
                             'wordperfect5.1', 'wsdl+xml', 'wspolicy+xml',
                             'x-www-form-urlencoded', 'x400-bp', 'xacml+xml',
                             'xcap-att+xml', 'xcap-caps+xml', 'xcap-diff+xml',
                             'xcap-el+xml', 'xcap-error+xml', 'xcap-ns+xml',
                             'xcon-conference-info-diff+xml',
                             'xcon-conference-info+xml', 'xenc+xml',
                             'xhtml+xml', 'xliff+xml', 'xml', 'xml-dtd',
                             'xml-external-parsed-entity', 'xml-patch+xml',
                             'xmpp+xml', 'xop+xml', 'xslt+xml', 'xv+xml',
                             'yang', 'yang-data+json', 'yang-data+xml',
                             'yang-patch+json','yang-patch+xml', 'yin+xml',
                             'zip', 'zlib', 'zstd']

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
