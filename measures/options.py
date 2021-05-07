import os, glob

external_libraries = ["--with%s" % p for p in ( "-aix-soname=aix",
                                                "-aix-soname=svr4",
                                                "-aix-soname=both",
                                                #"-ca-bundle",
                                                #"-ca-path", 
                                                #"-sysroot",
                                                "-gnu-ld",
                                                "-zlib",
                                                "-brotli",
                                                "-zstd",
                                                "-ldap-lib",
                                                "-lber-lib",
                                                "-default-ssl-backend=openssl",
                                                #"-winssl",
                                                #"-schannel",
                                                #"-darwinssl",
                                                #"-secure-transport",
                                                #"-amissl",
                                                "-ssl",
                                                #"-egd-socket",
                                                "-random",
                                                "-gnutls",
                                                "-mbedtls",
                                                #"-wolfssl",
                                                #"-mesalink",
                                                #"-bearssl",
                                                #"-rustls",
                                                "-nss",
                                                "-ca-fallback",
                                                "-libmetalink",
                                                "-libssh2",
                                                "-libssh",
                                                #"-wolfssh",
                                                "-librtmp",
                                                #"-winidn",
                                                "-libidn2",
                                                "-nghttp2",
                                                #"-ngtcp2",
                                                #"-nghttp3",
                                                #"-quiche",
                                                #"-hyper",
                                                "-zsh-functions-dir",
                                                "-fish-functions-dir",
                                                "-gssapi-includes",
                                                "-gssapi-libs",
                                                "-gssapi" #27
                                            )]


external_libraries_2 = ["--without%s" % p for p in ("-zlib",
                                                "-brotli",
                                                "-zstd",
                                                "-default-ssl-backend",
                                                #"-winssl",  
                                                #"-schannel",
                                                #"-darwinssl",
                                                #"-secure-transport",
                                                #"-amissl",
                                                "-ssl", # This was removed for sample configuration 8
                                                "-gnutls",
                                                "-mbedtls",
                                                #"-wolfssl",
                                                #"-mesalink",
                                                #"-bearssl",
                                                #"rustls",
                                                "-nss",
                                                "-ca-bundle",
                                                "-ca-path",
                                                "-ca-fallback",
                                                "-libpsl",
                                                "-libgsasl",
                                                "-libmetalink",
                                                "-librtmp",
                                                "-winidn",
                                                "-libidn2",
                                                "-nghttp2",
                                                #"-ngtcp2",
                                                #"-nghttp3",
                                                #"-quiche",
                                                #"-hyper",
                                                "-zsh-functions-dir",
                                                "-fish-functions-dir" #47
                                            )]

optional_features = ["--disable%s" % p for p in ("-silent-rules",
                                                "-debug",
                                                "-optimize",
                                                "-warnings",
                                                "-werror",
                                                "-curldebug",
                                                "-symbol-hiding",
                                                "-hidden-symbols",
                                                "-ares",
                                                "-rt",
                                                "-ech",
                                                "-dependency-tracking",
                                                "-largefile",
                                                "-libtool-lock",
                                                "-http",
                                                "-ftp",
                                                "-file",
                                                "-ldap",
                                                "-ldaps",
                                                "-rtsp",
                                                "-proxy",
                                                "-dict",
                                                "-telnet",
                                                "-tftp",
                                                "-pop3",
                                                "-imap",
                                                "-smb",
                                                "-smtp",
                                                "-gopher",
                                                "-mqtt",
                                                "-manual",
                                                "-libcurl-option",
                                                "-ipv6",
                                                "-openssl-auto-load-config",
                                                "-versioned-symbols",
                                                "-threaded-resolver",
                                                "-pthreads",
                                                "-verbose",
                                                "-sspi",
                                                "-ntlm-wb",
                                                "-tls-srp",
                                                "-unix-sockets",
                                                "-cookies",
                                                "-socketpair",
                                                "-http-auth",
                                                "-doh", #this was disabled to generate the sample configurations
                                                "-mime",
                                                "-dateparse",
                                                "-netrc",
                                                "-progress-meter",
                                                "-dnsshuffle",
                                                "-get-easy-options",
                                                "-alt-svc",
                                                "-hsts" #101
                                                )]
                                                # "-crypto-auth", //an error when using it. 
# Protocols: DICT FILE FTP FTPS GOPHER GOPHERS HTTP HTTPS IMAP IMAPS LDAP LDAPS MQTT POP3 POP3S RTMP RTSP SMB SMBS SMTP SMTPS TELNET TFTP
optional_features_2 = ["--enable%s" % p for p in (##"-maintainer-mode",
                                                ##"-silent-rules",
                                                ##"-debug",
                                                ##"-optimize",
                                                ##"-warnings",
                                                #"-werror",
                                                ##"-curldebug",
                                                ##"-symbol-hiding",
                                                ##"-hidden-symbols",
                                                ##"-ares",
                                                ##"-ech",
                                                ##"-code-coverage",
                                                ##"-dependency-tracking",
                                                #"-shared",
                                                "-static",
                                                "-fast-install"
                                                "-http",
                                                "-ftp",
                                                "-file",
                                                "-ldap",
                                                "-ldaps",
                                                "-rtsp",
                                                "-proxy",
                                                "-dict",
                                                "-telnet",
                                                "-tftp",
                                                "-pop3",
                                                "-imap",
                                                "-smb",
                                                "-smtp",
                                                "-gopher",
                                                "-mqtt",
                                                "-manual",
                                                "-libcurl-option",
                                                "-libgcc",
                                                "-ipv6",
                                                "-openssl-auto-load-config",
                                                "-versioned-symbols",
                                                "-threaded-resolver",
                                                "-pthreads",
                                                "-verbose",
                                                "-sspi",
                                                "-crypto-auth",
                                                "-ntlm-wb",
                                                "-tls-srp",
                                                "-unix-sockets",
                                                "-cookies",
                                                "-socketpair",
                                                "-http-auth",
                                                "-doh",
                                                "-mime",
                                                "-dateparse",
                                                "-netrc",
                                                "-progress-meter",
                                                "-dnsshuffle",
                                                "-get-easy-options",
                                                "-alt-svc",
                                                "-hsts" #158 - 2 = 156 options
                                                )]

# This is a sample configuration taken from the curl documentation, 
# suggested to use to reduce its binary size:
sample_configurations_01 = [["--disable-ares","--disable-cookies",
                            "--disable-ipv6","--disable-manual",
                            "--disable-proxy","--disable-unix-sockets",
                            "--disable-verbose","--disable-versioned-symbols",
                            "--enable-hidden-symbols","--without-libidn",
                            "--without-librtmp","--without-ssl",
                            "--without-zlib"]]

sample_configurations_02 = []
for l in external_libraries_2:
    sample_configurations_02.append(l)

for l in optional_features:
    sample_configurations_02.append(l)

# Adding the single configurations to an array 
def extractDigits(lst):
    res = []
    for el in lst:
        sub = el.split(', ')
        res.append(sub)
    print(res)
    return(res)
   

# All single configurations                   
single_configurations_01 = extractDigits(external_libraries)
single_configurations_02 = extractDigits(external_libraries_2)
single_configurations_03 = extractDigits(optional_features)
single_configurations_04 = extractDigits(optional_features_2)


# Adding the sample configuration sets (generated by FeatureIDE) to an array
sample_configurations = []

# for variant in glob.glob("measures/products/*.config"):
for variant in glob.glob("measures/products/*.config"):
    lineList = list()
    with open(variant) as f:
        for line in f:
            lineList = [line.rstrip('\n') for line in open(variant)]
        sample_configurations.append(lineList)

print(*single_configurations_01,*single_configurations_02,*single_configurations_04,*single_configurations_03)

# All single and sample configurations, 
# which will be used to measure the changes on
# the binary size and number of gadgets in x264
all_options =  [*single_configurations_04]