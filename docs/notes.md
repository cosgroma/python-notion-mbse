# Notes

## OMG Spec Page

```html
<!DOCTYPE html>
<html lang="en" class="js no-touch csstransforms3d csstransitions">
    <head>
        <title>
            About the XML Valuetype Language Mapping Specification Version 1.1
        </title>
        <link
            rel="alternate"
            type="application/json"
            href="https://www.omg.org/spec/XML/1.1/About-XML"
        />

        <meta charset="utf-8" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <link
            rel="canonical"
            href="https://www.omg.org/spec/XML/1.1/About-XML"
        />
        <link
            rel="alternate"
            type="application/rdf+xml"
            href="https://www.omg.org/spec/XML/1.1/About-XML"
        />
        <script type="application/ld+json">
            [
                {
                    "@id": "https://purl.org/dc/terms/license",
                    "@type": [
                        "http://www.w3.org/2002/07/owl#AnnotationProperty"
                    ]
                },
                {
                    "@id": "https://www.omg.org/spec/XML",
                    "@type": ["http://www.w3.org/2002/07/owl#NamedIndividual"],
                    "http://www.w3.org/1999/02/22-rdf-syntax-ns#type": [
                        {
                            "@id": "https://www.omg.org/techprocess/ab/SpecificationMetadata/Specification"
                        }
                    ],
                    "https://www.omg.org/techprocess/ab/SpecificationMetadata/category": [
                        {
                            "@value": "language-mapping"
                        },
                        {
                            "@value": "platform"
                        }
                    ],
                    "https://www.omg.org/techprocess/ab/SpecificationMetadata/publicationDate": [
                        {
                            "@type": "http://www.w3.org/2001/XMLSchema#dateTime",
                            "@value": "2003-04-01T00:00:00-0500"
                        }
                    ],
                    "https://www.omg.org/techprocess/ab/SpecificationMetadata/specificationAbbreviation": [
                        {
                            "@value": "XML"
                        }
                    ],
                    "https://www.omg.org/techprocess/ab/SpecificationMetadata/specificationAbstract": [
                        {
                            "@value": "This specification provides two essential scenarios for using XML to create IDL valuetypes. The first scenario, where dynamic information is present, leverages existing standards to provide access to the full contents of an XML document in terms of IDL valuetypes. The second scenario builds upon the first where additional static information is present from XML DTDs and (in the future) XML Schemas. The DTDs / Schemas are metadata used to generate Valuetypes that match the types of information expected to be present in XML documents."
                        }
                    ],
                    "https://www.omg.org/techprocess/ab/SpecificationMetadata/specificationTitle": [
                        {
                            "@value": "XML Valuetype Language Mapping"
                        }
                    ],
                    "https://www.omg.org/techprocess/ab/SpecificationMetadata/specificationURL": [
                        {
                            "@id": "https://www.omg.org/spec/XML/About-XML"
                        }
                    ]
                },
                {
                    "@id": "https://www.omg.org/spec/XML/About-XML",
                    "@type": ["http://www.w3.org/2002/07/owl#Ontology"],
                    "http://www.w3.org/2000/01/rdf-schema#label": [
                        {
                            "@value": "About the XML Valuetype Language Mapping Specification Version 1.1"
                        }
                    ],
                    "http://www.w3.org/2002/07/owl#imports": [
                        {
                            "@id": "https://www.omg.org/techprocess/ab/SpecificationMetadata/"
                        }
                    ],
                    "http://www.w3.org/2002/07/owl#versionIRI": [
                        {
                            "@id": "https://www.omg.org/spec/XML/1.1/About-XML"
                        }
                    ],
                    "http://www.w3.org/2002/07/owl#versionInfo": [
                        {
                            "@value": "Generated on 2024-06-22T20:19:10-0400"
                        }
                    ],
                    "https://purl.org/dc/terms/license": [
                        {
                            "@id": "https://www.omg.org/techprocess/ab/SpecificationMetadata/MITLicense"
                        }
                    ],
                    "https://www.omg.org/techprocess/ab/SpecificationMetadata/creationDate": [
                        {
                            "@type": "http://www.w3.org/2001/XMLSchema#dateTime",
                            "@value": "2003-04-01T00:00:00-0500"
                        }
                    ],
                    "https://www.omg.org/techprocess/ab/SpecificationMetadata/filename": [
                        {
                            "@value": "About-XML"
                        }
                    ]
                },
                {
                    "@id": "https://www.omg.org/techprocess/ab/SpecificationMetadata/Specification",
                    "@type": ["http://www.w3.org/2002/07/owl#Class"]
                },
                {
                    "@id": "https://www.omg.org/techprocess/ab/SpecificationMetadata/category",
                    "@type": [
                        "http://www.w3.org/2002/07/owl#AnnotationProperty"
                    ]
                },
                {
                    "@id": "https://www.omg.org/techprocess/ab/SpecificationMetadata/creationDate",
                    "@type": [
                        "http://www.w3.org/2002/07/owl#AnnotationProperty"
                    ]
                },
                {
                    "@id": "https://www.omg.org/techprocess/ab/SpecificationMetadata/filename",
                    "@type": [
                        "http://www.w3.org/2002/07/owl#AnnotationProperty"
                    ]
                },
                {
                    "@id": "https://www.omg.org/techprocess/ab/SpecificationMetadata/publicationDate",
                    "@type": [
                        "http://www.w3.org/2002/07/owl#AnnotationProperty"
                    ]
                },
                {
                    "@id": "https://www.omg.org/techprocess/ab/SpecificationMetadata/specificationAbbreviation",
                    "@type": [
                        "http://www.w3.org/2002/07/owl#AnnotationProperty"
                    ]
                },
                {
                    "@id": "https://www.omg.org/techprocess/ab/SpecificationMetadata/specificationAbstract",
                    "@type": [
                        "http://www.w3.org/2002/07/owl#AnnotationProperty"
                    ]
                },
                {
                    "@id": "https://www.omg.org/techprocess/ab/SpecificationMetadata/specificationTitle",
                    "@type": [
                        "http://www.w3.org/2002/07/owl#AnnotationProperty"
                    ]
                },
                {
                    "@id": "https://www.omg.org/techprocess/ab/SpecificationMetadata/specificationURL",
                    "@type": [
                        "http://www.w3.org/2002/07/owl#AnnotationProperty"
                    ]
                }
            ]
        </script>

        <script src="https://www.omg.org/js/privacy.js"></script>

        <!-- HEAD INCLUDE BEGIN -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />

        <!-- Mobile Specific Metas
    ================================================== -->
        <meta
            name="viewport"
            content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0"
        />

        <!-- Google Web Fonts
    ================================================== -->
        <link
            href="//fonts.googleapis.com/css?family=Anton|Muli:300,400,400italic,300italic|Oswald"
            rel="stylesheet"
            type="text/css"
        />

        <!-- Google tag (gtag.js) -->
        <script
            async
            src="https://www.googletagmanager.com/gtag/js?id=G-3FR65VLKVW"
        ></script>
        <script>
            window.dataLayer = window.dataLayer || [];

            function gtag() {
                dataLayer.push(arguments);
            }

            gtag("js", new Date());
            gtag("config", "G-3FR65VLKVW");
        </script>
        <!-- Google Tag Manager -->
        <script>
            (function (w, d, s, l, i) {
                w[l] = w[l] || [];
                w[l].push({
                    "gtm.start": new Date().getTime(),
                    event: "gtm.js",
                });
                var f = d.getElementsByTagName(s)[0],
                    j = d.createElement(s),
                    dl = l != "dataLayer" ? "&l=" + l : "";
                j.async = true;
                j.src = "https://www.googletagmanager.com/gtm.js?id=" + i + dl;
                f.parentNode.insertBefore(j, f);
            })(window, document, "script", "dataLayer", "GTM-P67F35Z");
        </script>
        <!-- End Google Tag Manager -->

        <!-- Global Site Tag (gtag.js) - Google Analytics -->
        <script
            async
            src="https://www.googletagmanager.com/gtag/js?id=UA-106941488-1"
        ></script>
        <script>
            window.dataLayer = window.dataLayer || [];

            function gtag() {
                dataLayer.push(arguments);
            }

            gtag("js", new Date());
            gtag("config", "UA-106941488-1");
        </script>
        <!-- Google Analytics -->

        <!-- CSS
    ================================================== -->
        <!-- Base + Vendors CSS -->
        <link
            href="https://www.omg.org/css/bootstrap.min.css"
            rel="stylesheet"
        />
        <link
            href="https://www.omg.org/css/fonts/font-awesome/css/font-awesome.css"
            rel="stylesheet"
        />
        <link
            href="https://www.omg.org/vendor/owl-carousel/owl.carousel.css"
            media="screen"
            rel="stylesheet"
        />
        <link
            href="https://www.omg.org/vendor/owl-carousel/owl.theme.css"
            media="screen"
            rel="stylesheet"
        />
        <link
            href="https://www.omg.org/vendor/magnific-popup/magnific-popup.css"
            media="screen"
            rel="stylesheet"
        />
        <link
            href="https://www.omg.org/vendor/mediaelement/mediaelementplayer.css"
            rel="stylesheet"
        />

        <!-- Theme CSS-->
        <link href="https://www.omg.org/css/theme.css" rel="stylesheet" />
        <link
            href="https://www.omg.org/css/theme-elements.css"
            rel="stylesheet"
        />
        <link href="https://www.omg.org/css/animate.min.css" rel="stylesheet" />

        <!-- Skin CSS -->
        <link href="https://www.omg.org/css/skins/teal.css" rel="stylesheet" />

        <!-- Custom CSS-->
        <link href="https://www.omg.org/css/custom.css" rel="stylesheet" />

        <!-- Head Libs -->
        <script src="https://www.omg.org/vendor/modernizr.js"></script>

        <!--[if lt IE 9]>
            <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
            <script src="vendor/respond.min.js"></script>
        <![endif]-->

        <!--[if IE]>
            <link rel="stylesheet" href="css/ie.css" />
        <![endif]-->

        <!-- Favicons
    ================================================== -->
        <link rel="shortcut icon" href="//www.omg.org/images/favicon.ico" />
        <link rel="icon" href="//www.omg.org/images/apple-touch-icon.png" />
        <link
            rel="icon"
            sizes="72x72"
            href="//www.omg.org/images/apple-touch-icon-72x72.png"
        />
        <link
            rel="icon"
            sizes="114x114"
            href="//www.omg.org/images/apple-touch-icon-114x114.png"
        />
        <link
            rel="icon"
            sizes="144x144"
            href="//www.omg.org/images/apple-touch-icon-144x144.png"
        />

        <!-- sortable tables -->
        <link
            href="https://unpkg.com/bootstrap-table@1.18.3/dist/bootstrap-table.min.css"
            rel="stylesheet"
        />

        <!-- InstanceBeginEditable name="head" -->
        <!-- InstanceEndEditable -->
        <style id="fit-vids-style">
            .fluid-width-video-wrapper {
                width: 100%;
                position: relative;
                padding: 0;
            }
            .fluid-width-video-wrapper iframe,
            .fluid-width-video-wrapper object,
            .fluid-width-video-wrapper embed {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
            }
        </style>
        <style type="text/css">
            .st-install-UJwkmPzgjHBCxHyxzCaj .st-ui-result,
            .st-ui-type-heading {
                color: #0089d7 !important;
            }
            .st-install-UJwkmPzgjHBCxHyxzCaj .st-ui-result em {
                font-style: normal;
                font-weight: bold;
                background-color: #f6fcfe !important;
            }

            ul.dd-list {
                margin-bottom: 0;
            }
        </style>
        <script
            type="text/javascript"
            src="//script.crazyegg.com/pages/scripts/0104/8617.js"
            async="async"
        ></script>
        <!-- HEAD INCLUDE END -->
    </head>
    <body onload="getOMGCookie('omgprivacy');">
        <!-- Google Tag Manager (noscript) -->
        <noscript>
            <iframe
                src="https://www.googletagmanager.com/ns.html?id=GTM-P67F35Z"
                height="0"
                width="0"
                style="display: none; visibility: hidden"
            ></iframe>
        </noscript>
        <!-- End Google Tag Manager (noscript) -->

        <!-- BODY HEADER INCLUDE BEGIN -->
        <header class="header header-default">
            <div class="header-top">
                <div class="container">
                    <div class="header-top-left">
                        <ul class="header-top-nav">
                            <li>
                                <a href="https://www.omg.org/index.htm"
                                    ><span style="color: white">Home</span></a
                                >
                            </li>
                            <li>
                                <i class="fa fa-lock" aria-hidden="true"></i
                                ><a
                                    onclick="ga('send', 'event', 'Home', 'click', 'Member Area Login');"
                                    href="https://www.omg.org/members/"
                                    ><span style="color: white"
                                        >Member Area Login</span
                                    ></a
                                >
                            </li>
                            <!--<li><a onClick="ga('send', 'event', 'Home', 'click', 'Legal');" href="legal/index.htm"><span style="color:white">Legal</span></a></li>-->
                        </ul>
                        <ul class="header-top-nav">
                            <li>
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                <a
                                    onclick="ga('send', 'event', 'Home', 'click', 'Blog Icon');"
                                    href="https://www.objectmanagementgroup.org/blog/?__hstc=108882653.c57f72fd8a7d413e47334a401ea57c55.1689194386374.1715633757428.1717974653794.293&amp;__hssc=108882653.13.1717974653794&amp;__hsfp=3194928710"
                                    ><i
                                        class="fa fa-pencil-square-o"
                                        aria-hidden="true"
                                    ></i></a
                                >&nbsp;&nbsp;<a
                                    onclick="ga('send', 'event', 'Home', 'click', 'BrightTalk');"
                                    href="https://www.brighttalk.com/channel/12231/"
                                    ><i
                                        class="fa fa-bold"
                                        aria-hidden="true"
                                    ></i></a
                                >&nbsp;&nbsp;<a
                                    onclick="ga('send', 'event', 'Home', 'click', 'LinkedIn');"
                                    href="https://sg.linkedin.com/company/omg"
                                    ><i
                                        class="fa fa-linkedin"
                                        aria-hidden="true"
                                    ></i></a
                                >&nbsp;&nbsp;<a
                                    onclick="ga('send', 'event', 'Home', 'click', 'Twitter');"
                                    href="https://twitter.com/objectmgmtgroup"
                                    ><i
                                        class="fa-brands fa-x-twitter"
                                        aria-hidden="true"
                                    ></i></a
                                >&nbsp;&nbsp;<a
                                    onclick="ga('send', 'event', 'Home', 'click', 'Youtube');"
                                    href="https://www.youtube.com/user/ObjectMgmtGroup/videos"
                                    ><i
                                        class="fa fa-youtube"
                                        aria-hidden="true"
                                    ></i
                                ></a>
                            </li>
                        </ul>
                    </div>
                    <div class="header-top-right">
                        <!-- AddSearch -->

                        <script src="https://addsearch.com/js/?key=a77fb1eb2c3c8fafe2b301824369ed97&amp;categories=0xwww.omg.org"></script>
                        <input
                            type="text"
                            value=""
                            style="
                                cursor: auto;
                                background-color: rgb(255, 255, 255);
                                background-image: url('//addsearch.com/logo/AAAAAA-20.png');
                                background-repeat: no-repeat;
                                background-position: 95% 50%;
                                display: inline-block;
                                width: 190px;
                                height: 16px;
                                padding: 7px 11px 7px 28px;
                                border: 1px solid rgba(0, 0, 0, 0.25);
                                font-weight: 400;
                                color: rgb(59, 69, 79);
                                font-size: 14px;
                                line-height: 16px;
                                box-sizing: content-box;
                                background-clip: padding-box;
                                border-radius: 5px;
                                box-shadow: none;
                            "
                            class="addsearch addsearch-written"
                            data-addsearch-field="true"
                            autocomplete="off"
                            aria-label="Search field"
                        />

                        <!-- AddSearch -->
                    </div>
                </div>
            </div>
            <div class="header-main">
                <div class="container">
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <title>Menu | Object Management Group</title>
                            <meta
                                name="description"
                                content="Menu - Object Management Group"
                            />
                        </head>
                        <body>
                            <nav class="navbar navbar-default fhmm">
                                <div class="navbar-header">
                                    <button type="button" class="navbar-toggle">
                                        <i class="fa fa-bars"></i>
                                    </button>
                                    <!-- Logo -->
                                    <div class="logo">
                                        <!--<a href="index.htm"><img src="images/logos/OMG-logo-web-sm.svg" alt="OMG logo"></a>-->
                                        <a href="https://www.omg.org/index.htm"
                                            ><img
                                                src="https://www.omg.org/images/logos/OMG-logo-web-sm.svg"
                                                alt="OMG logo"
                                        /></a>
                                    </div>
                                    <!-- Logo / End -->
                                </div>
                                <!-- end navbar-header -->
                                <div
                                    id="main-nav"
                                    class="navbar-collapse collapse"
                                >
                                    <ul class="nav navbar-nav">
                                        <!-- About -->
                                        <li class="dropdown">
                                            <a
                                                href="#"
                                                data-toggle="dropdown"
                                                class="dropdown-toggle"
                                                >About Us <b class="caret"></b
                                            ></a>
                                            <ul
                                                class="dropdown-menu"
                                                role="menu"
                                            >
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'Home', 'click', 'MENU About Overview');"
                                                        href="https://www.omg.org/about/"
                                                        >Overview</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'Home', 'click', 'MENU Staff');"
                                                        href="https://www.omg.org/about/staff.htm"
                                                        >Meet our Staff</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'Home', 'click', 'MENU Structure');"
                                                        href="https://www.omg.org/about/structure-and-governance.htm"
                                                        >Structure and
                                                        Governance</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'Home', 'click', 'SDO Standards Process');"
                                                        href="https://www.omg.org/about/sdo-standards-process.htm"
                                                        >SDO Standards
                                                        Process</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'Home', 'click', 'MENU Our Specifications');"
                                                        href="https://www.omg.org/spec/"
                                                        >Our Specifications</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'Home', 'click', 'MENU OMG Story');"
                                                        href="https://www.objectmanagementgroup.org/"
                                                        >OMG Story</a
                                                    >
                                                </li>
                                            </ul>
                                            <!-- end row -->
                                        </li>
                                        <!-- About Ends -->
                                        <!-- Programs -->
                                        <li
                                            class="dropdown dropdown-left fhmm-fw"
                                        >
                                            <a
                                                href="#"
                                                data-toggle="dropdown"
                                                class="dropdown-toggle"
                                                >Groups <b class="caret"></b
                                            ></a>
                                            <ul
                                                class="dropdown-menu half half-left"
                                            >
                                                <li
                                                    class="fhmm-content withoutdesc"
                                                >
                                                    <div class="row">
                                                        <div class="col-sm-6">
                                                            <h3 class="title">
                                                                <a
                                                                    href="https://www.omg.org/about/dtc.htm"
                                                                    >Domain
                                                                    Technology
                                                                    Committee</a
                                                                >
                                                            </h3>
                                                            <ul>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/bmi/"
                                                                        >Business</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/ocs/"
                                                                        >Civic</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/c4i/"
                                                                        >Defense
                                                                        &amp;
                                                                        Military</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/fdtf/"
                                                                        >Financial
                                                                        Sector</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/gov/"
                                                                        >Government</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/healthcare/"
                                                                        >Healthcare</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/mantis/"
                                                                        >Manufacturing</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/maths/"
                                                                        >Mathematical</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/retail/"
                                                                        >Retail</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/robotics/"
                                                                        >Robotics</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/space/"
                                                                        >Space</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/syseng/"
                                                                        >Systems
                                                                        Engineering</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/uaf/"
                                                                        >Unified
                                                                        Architecture
                                                                        Framework</a
                                                                    >
                                                                </li>
                                                            </ul>
                                                        </div>
                                                        <div class="col-sm-6">
                                                            <h3 class="title">
                                                                <a
                                                                    href="https://www.omg.org/about/ptc.htm"
                                                                    >Platform
                                                                    Technology
                                                                    Committee</a
                                                                >
                                                            </h3>
                                                            <ul>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/agent/"
                                                                        >Agency</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/ai/"
                                                                        >AI</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/adtf/"
                                                                        >Analysis
                                                                        &amp;
                                                                        Design</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/adm/"
                                                                        >Architecture-Driven
                                                                        Modernization</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/cloud/"
                                                                        >Cloud</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/dds/"
                                                                        >Data
                                                                        Distribution
                                                                        Services</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/ekg/"
                                                                        >Enterprise
                                                                        Knowledge
                                                                        Graph</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/methods-and-tools/"
                                                                        >Methods
                                                                        &amp;
                                                                        Tools</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/mars/"
                                                                        >Middleware</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/ontology/"
                                                                        >Ontology</a
                                                                    >
                                                                </li>
                                                                <li>
                                                                    <a
                                                                        href="https://www.omg.org/sysa/"
                                                                        >Systems
                                                                        Assurance</a
                                                                    >
                                                                </li>
                                                            </ul>
                                                        </div>
                                                    </div>
                                                    <!-- end row -->
                                                </li>
                                                <!-- end grid demo -->
                                            </ul>
                                            <!-- end drop down menu -->
                                        </li>
                                        <!-- Programs -->
                                        <!-- Certifications -->
                                        <li class="dropdown">
                                            <a
                                                href="#"
                                                data-toggle="dropdown"
                                                class="dropdown-toggle"
                                                >Certifications
                                                <b class="caret"></b
                                            ></a>
                                            <ul
                                                class="dropdown-menu"
                                                role="menu"
                                            >
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU CERT MAIN');"
                                                        href="https://www.omg.org/certification/"
                                                        >Overview</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU OCEB 2');"
                                                        href="https://www.omg.org/certification/bpm/"
                                                        >Business Process
                                                        Management</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU CBA');"
                                                        href="https://www.businessarchitectureguild.org/page/certification"
                                                        target="_blank"
                                                        >Certified Business
                                                        Architect</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU OCSMP');"
                                                        href="https://www.omg.org/certification/sysml/"
                                                        >Systems Modeling
                                                        Language</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU OCUP 2');"
                                                        href="https://www.omg.org/certification/uml/"
                                                        >Unified Modeling
                                                        Language</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Training');"
                                                        href="https://www.omg.org/certification/training/"
                                                        >Training</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'Home', 'click', 'MENU Discounts');"
                                                        href="https://www.omg.org/certification/certification-exam-discounts/"
                                                        >Exam Discounts</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU BPMplus Cert Sponsorship');"
                                                        href="https://www.omg.org/certification/bpm/sponsorship/"
                                                        >BPM&#43; Sponsorship</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU SysML Cert Sponsorship');"
                                                        href="https://www.omg.org/certification/sysml/sponsorship"
                                                        >SysML Sponsorship</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU UAF Cert Sponsorship');"
                                                        href="https://www.omg.org/certification/uaf/sponsorship/"
                                                        >UAF Sponsorship</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Certified Professionals Directory');"
                                                        href="https://www.credly.com/organizations/omg/directory"
                                                        target="_blank"
                                                        >Certified Professionals
                                                        Directory</a
                                                    >
                                                </li>
                                            </ul>
                                            <!-- end row -->
                                        </li>
                                        <!-- Certifications -->
                                        <!-- Resource Hub menu -->
                                        <li class="dropdown">
                                            <a
                                                href="#"
                                                data-toggle="dropdown"
                                                class="dropdown-toggle"
                                                >Resources <b class="caret"></b
                                            ></a>
                                            <ul
                                                class="dropdown-menu"
                                                role="menu"
                                            >
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Blog');"
                                                        href="https://www.objectmanagementgroup.org/blog/"
                                                        >Blog</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU OMG Brochure');"
                                                        href="https://www.omg.org/memberservices/OMG-brochure.pdf"
                                                        >Brochure</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Events');"
                                                        href="https://www.omg.org/events/index.htm"
                                                        >Events</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Journal of Innovation');"
                                                        href="https://www.objectmanagementgroup.org/journal-of-innovation/"
                                                        >Journal of
                                                        Innovation</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Press Room');"
                                                        href="https://www.omg.org/news/pressroom.htm"
                                                        >Press Room</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Processes');"
                                                        href="https://www.omg.org/gettingstarted/processintro.htm"
                                                        >Processes</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Public Document Search');"
                                                        href="https://www.omg.org/cgi-bin/apps/doclist.pl"
                                                        >Public Document
                                                        Search</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Member Document Search');"
                                                        href="https://www.omg.org/members_docsearch.htm"
                                                        >Member Document
                                                        Search</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU TermsAcronyms');"
                                                        href="https://www.omg.org/gettingstarted/terms_and_acronyms.htm"
                                                        >Terms &amp; Acronyms
                                                    </a>
                                                </li>
                                                <!--<li><a onClick="ga('send', 'event', 'click', 'MENU Vendor Directories');" href="https://www.omg.org/omg-directories.htm">Vendor Directories</a></li>-->
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Webinars');"
                                                        href="https://www.omg.org/webinars/index.htm"
                                                        >Webinars</a
                                                    >
                                                </li>
                                            </ul>
                                        </li>
                                        <!-- Resource Hub menu -->
                                        <!-- Specs -->
                                        <li class="dropdown">
                                            <a
                                                href="#"
                                                data-toggle="dropdown"
                                                class="dropdown-toggle"
                                                >Specifications
                                                <b class="caret"></b
                                            ></a>
                                            <ul
                                                class="dropdown-menu"
                                                role="menu"
                                            >
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Popular');"
                                                        href="https://www.omg.org/about/omg-standards-introduction.htm"
                                                        >Popular</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Catalog');"
                                                        href="https://www.omg.org/spec/"
                                                        >Catalog</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU In Progress');"
                                                        href="https://www.omg.org/public_schedule/"
                                                        >In Progress</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Issues');"
                                                        href="https://issues.omg.org/issues/lists"
                                                        >Issues</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Report Issues');"
                                                        href="https://issues.omg.org/issues/create-new-issue"
                                                        >Report Issue(s)</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU RFC Comments');"
                                                        href="https://www.omg.org/technology/rfc-form.htm"
                                                        >RFC Comments</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Vote Status');"
                                                        href="https://www.omg.org/techprocess/faxvotes/"
                                                        target="_blank"
                                                        >Vote Status</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Archive');"
                                                        href="https://www.omg.org/technology/documents/vault.htm"
                                                        >Archive</a
                                                    >
                                                </li>
                                            </ul>
                                        </li>
                                        <!-- Specs -->
                                        <!-- Communities -->
                                        <li class="dropdown">
                                            <a
                                                href="#"
                                                data-toggle="dropdown"
                                                class="dropdown-toggle"
                                                >Communities
                                                <b class="caret"></b
                                            ></a>
                                            <ul
                                                class="dropdown-menu"
                                                role="menu"
                                            >
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'Home', 'click', 'MENU Communities');"
                                                        href="https://www.omg.org/communities/index.htm"
                                                        >Managed Communities</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'Home', 'click', 'MENU Communities EKG');"
                                                        href="https://www.omg.org/communities/enterprise-knowledge-graph-forum.htm"
                                                        >The Enterprise
                                                        Knowledge Graph Forum</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'Home', 'click', 'MENU Communities MBSE');"
                                                        href="https://www.omg.org/communities/model-based-acquisition-user-community.htm"
                                                        >Model-Based Acquisition
                                                        User Group</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'Home', 'click', 'MENU Communities SysEng');"
                                                        href="https://www.omg.org/communities/systems-modeling-community.htm"
                                                        >Systems Modeling</a
                                                    >
                                                </li>
                                            </ul>
                                            <!-- end row -->
                                        </li>
                                        <!-- Communities -->
                                        <!-- Membership -->
                                        <li class="dropdown">
                                            <a
                                                href="#"
                                                data-toggle="dropdown"
                                                class="dropdown-toggle"
                                                >Membership <b class="caret"></b
                                            ></a>
                                            <ul
                                                class="dropdown-menu"
                                                role="menu"
                                            >
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Become a Member');"
                                                        href="https://www.omg.org/memberservices/index.htm"
                                                        >Become a Member</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Current Members');"
                                                        href="https://www.omg.org/cgi-bin/apps/membersearch.pl"
                                                        >Current Members</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Member Partners');"
                                                        href="https://www.omg.org/about/liaison.htm"
                                                        >Liaisons</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Member Sponsorship');"
                                                        href="https://www.omg.org/memberservices/sponsorship.htm"
                                                        >Sponsorship</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Log In');"
                                                        href="https://www.omg.org/members/"
                                                        ><i
                                                            class="fa fa-lock"
                                                        ></i
                                                        >Log-In</a
                                                    >
                                                </li>
                                                <li>
                                                    <a
                                                        onclick="ga('send', 'event', 'click', 'MENU Log In Assistance');"
                                                        href="https://www.omg.org/login/index.htm"
                                                        ><i
                                                            class="fa fa-unlock"
                                                        ></i
                                                        >Log-In Assistance</a
                                                    >
                                                </li>
                                            </ul>
                                        </li>
                                        <!-- Membership -->
                                    </ul>
                                    <!-- end nav navbar-nav -->
                                </div>
                                <!-- end #main-nav -->
                            </nav>
                            <!-- end navbar navbar-default fhmm -->
                        </body>
                    </html>
                </div>
            </div>
        </header>
        <!-- BODY HEADER INCLUDE END -->

        <div class="main" role="main">
            <!-- Main -->
            <section class="page-heading" role="navigation">
                <div class="container">
                    <div class="row">
                        <div class="col-md-9">
                            <h1>
                                About the XML Valuetype Language Mapping
                                Specification Version 1.1
                            </h1>
                        </div>
                        <div class="col-md-3">
                            <ul role="menu" class="breadcrumb">
                                <li role="menuitem" class="active">1.1</li>
                                <li role="menuitem" class="active">XML</li>

                                <li role="menuitem">
                                    <a href="https://www.omg.org/spec"
                                        >Specifications</a
                                    >
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>
            <div class="page-content" role="directory">
                <section
                    id="document-metadata"
                    role="complementary"
                    class="container"
                >
                    <div class="container">
                        <h1 class="spec-acronym col-md-3">XML</h1>
                        <h1 class="spec-name" style="text-transform: none">
                            XML Valuetype Language Mapping
                        </h1>
                    </div>
                    <div class="container">
                        <div class="col-md-11">
                            <p class="text-justify">
                                This specification provides two essential
                                scenarios for using XML to create IDL
                                valuetypes. The first scenario, where dynamic
                                information is present, leverages existing
                                standards to provide access to the full contents
                                of an XML document in terms of IDL valuetypes.
                                The second scenario builds upon the first where
                                additional static information is present from
                                XML DTDs and (in the future) XML Schemas. The
                                DTDs / Schemas are metadata used to generate
                                Valuetypes that match the types of information
                                expected to be present in XML documents.
                            </p>
                            <dl class="dl-horizontal">
                                <!-- title -->
                                <dt>Title:</dt>
                                <dd>XML Valuetype Language Mapping</dd>

                                <!-- acronym -->
                                <dt>Acronym:</dt>
                                <dd>XML</dd>

                                <!-- version -->
                                <dt>Version:</dt>
                                <dd>
                                    <p style="margin-bottom: 0">
                                        <span>1.1</span>
                                    </p>
                                </dd>
                                <!-- document status -->
                                <dt>Document Status:</dt>
                                <dd>
                                    <p style="margin-bottom: 0">
                                        <span
                                            data-toggle="tooltip"
                                            data-placement="right"
                                            data-container="body"
                                            title="Formal Specifications have been approved by OMG Board of Directors and have been edited."
                                            >formal ⓘ</span
                                        >
                                    </p>
                                </dd>

                                <!-- publication date -->
                                <dt>Publication Date:</dt>
                                <dd>April 2003</dd>

                                <!-- categories -->
                                <dt>Categories:</dt>
                                <dd>
                                    <ul
                                        role="group"
                                        class="list-inline dd-list"
                                    >
                                        <li
                                            role="listitem"
                                            class="text-capitalize"
                                        >
                                            <a
                                                class="badge badge-info"
                                                href="https://www.omg.org/spec/category/language-mapping"
                                                ><em>Language Mapping</em></a
                                            >
                                        </li>
                                        <li
                                            role="listitem"
                                            class="text-capitalize"
                                        >
                                            <a
                                                class="badge badge-info"
                                                href="https://www.omg.org/spec/category/platform"
                                                ><em>Platform</em></a
                                            >
                                        </li>
                                    </ul>
                                </dd>
                            </dl>
                        </div>
                        <!-- Specification documents -->
                        <div class="col-md-1">
                            <div style="text-align: center; margin-bottom: 5px">
                                <a
                                    class="download-document"
                                    href="https://www.omg.org/spec/XML/1.1/PDF"
                                    title="Click to Download Specificaton Document"
                                    data-spec="XML/1.1"
                                    data-label="XML/1.1/PDF"
                                >
                                    <i class="fa fa-file-pdf-o fa-3x"></i><br />
                                    Specification
                                </a>
                            </div>
                        </div>
                    </div>
                    <hr class="container”/" />
                </section>

                <!-- Table of Contents -->
                <section id="toc" class="container">
                    <h2 role="heading" aria-level="1">Table Of Contents</h2>
                    <ul role="directory" class="toc">
                        <li class="tocline">
                            <a class="text-info" href="#document-metadata"
                                >About the Specification</a
                            >
                        </li>
                        <li class="tocline">
                            <a class="text-info" href="#companies"
                                >Companies that have contributed to the
                                development of this Specification</a
                            >
                        </li>
                        <li class="tocline">
                            <a class="text-info" href="#issues"
                                >Issues associated with this specification</a
                            >
                        </li>
                        <li class="tocline">
                            <a class="text-info" href="#documents"
                                >Specification Documents</a
                            >
                            <ul class="toc">
                                <li class="tocline">
                                    <a
                                        class="text-info"
                                        href="#docs-normative-supporting"
                                        >Normative Documents</a
                                    >
                                </li>
                            </ul>
                        </li>
                        <li class="tocline">
                            <a class="text-info" href="#spec-versions"
                                >History</a
                            >
                            <ul class="toc">
                                <li class="tocline">
                                    <a
                                        class="text-info"
                                        href="#spec-versions-formal"
                                        >Formal Versions</a
                                    >
                                </li>
                            </ul>
                        </li>
                        <li class="tocline">
                            <a class="text-info" href="#inventory-links"
                                >Links</a
                            >
                        </li>
                    </ul>
                    <hr class="container”/" />
                </section>
                <section id="companies" class="container">
                    <h2 role="heading" aria-level="1">
                        Companies that have contributed to the development of
                        this Specification
                    </h2>
                    <ul role="directory" class="toc">
                        <li class="tocline">
                            Copyright © 2000
                            <a
                                class="text-info"
                                href="https://www.omg.org/spec/company/bea-systems/"
                                >BEA Systems</a
                            >
                        </li>
                        <li class="tocline">
                            Copyright © 2000
                            <a
                                class="text-info"
                                href="https://www.omg.org/spec/company/cape-clear-software-limited/"
                                >Cape Clear Software Limited</a
                            >
                        </li>
                        <li class="tocline">
                            Copyright © 2000
                            <a
                                class="text-info"
                                href="https://www.omg.org/spec/company/hewlett-packard/"
                                >Hewlett Packard</a
                            >
                        </li>
                        <li class="tocline">
                            Copyright © 2000
                            <a
                                class="text-info"
                                href="https://www.omg.org/spec/company/iona-technologies-inc./"
                                >IONA Technologies Inc.</a
                            >
                        </li>
                        <li class="tocline">
                            Copyright © 2000
                            <a
                                class="text-info"
                                href="https://www.omg.org/spec/company/international-business-machines-corporation/"
                                >International Business Machines Corporation</a
                            >
                        </li>
                        <li class="tocline">
                            Copyright © 2000
                            <a
                                class="text-info"
                                href="https://www.omg.org/spec/company/oracle-corporation/"
                                >Oracle Corporation</a
                            >
                        </li>
                        <li class="tocline">
                            Copyright © 2000
                            <a
                                class="text-info"
                                href="https://www.omg.org/spec/company/peerlogic/"
                                >PeerLogic</a
                            >
                        </li>
                        <li class="tocline">
                            Copyright © 2000
                            <a
                                class="text-info"
                                href="https://www.omg.org/spec/company/persistence-software/"
                                >Persistence Software</a
                            >
                        </li>
                        <li class="tocline">
                            Copyright © 2000
                            <a
                                class="text-info"
                                href="https://www.omg.org/spec/company/rogue-wave-software/"
                                >Rogue Wave Software</a
                            >
                        </li>
                        <li class="tocline">
                            Copyright © 2000
                            <a
                                class="text-info"
                                href="https://www.omg.org/spec/company/unisys-corporation/"
                                >Unisys Corporation</a
                            >
                        </li>
                    </ul>
                    <hr class="container”/" />
                </section>
                <section id="issues" class="container">
                    <h2 role="heading" aria-level="1">
                        Issues associated with this specification
                    </h2>
                    <div class="container issues-links">
                        <p class="col-md-2">
                            <a href="https://issues.omg.org/issues/spec/XML">
                                <i class="fa fa-list fa-3x"></i><br />
                                Issues Reported in this Specification </a
                            >&nbsp;&dash;
                            <br />
                            <em>
                                <a
                                    href="https://issues.omg.org/issues/spec/XML/1.1"
                                >
                                    Version 1.1 only
                                </a>
                            </em>
                        </p>
                        <p class="col-md-2">
                            <a
                                href="https://issues.omg.org/issues/spec/XML/fixed"
                            >
                                <i class="fa fa-flag-checkered fa-3x"></i><br />
                                Issues Fixed in this Specification </a
                            >&nbsp;&dash;
                            <br />
                            <em>
                                <a
                                    href="https://issues.omg.org/issues/spec/XML/1.1/fixed"
                                >
                                    Version 1.1 only
                                </a>
                            </em>
                        </p>
                        <p class="col-md-2">
                            <a
                                href="https://issues.omg.org/issues/create-new-issue?specification=XML%231.1"
                            >
                                <i class="fa fa-commenting fa-3x"></i><br />
                                Report an issue
                            </a>
                        </p>
                    </div>
                    <hr class="container”/" />
                </section>

                <section id="documents" class="container">
                    <h2 role="heading" aria-level="1">
                        Specification Documents
                    </h2>
                    <section class="container" id="docs-normative-supporting">
                        <h3 role="heading" aria-level="2">
                            Normative Documents
                        </h3>
                        <div class="table-responsive">
                            <table class="table table-striped" data-sortable>
                                <thead>
                                    <tr>
                                        <th class="col-xs-5">Description</th>
                                        <th class="col-xs-1">Format</th>
                                        <th class="col-xs-3">URL</th>
                                        <th class="col-xs-2">OMG File ID</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td class="document-explanation">
                                            Specification
                                        </td>
                                        <td class="document-format">PDF</td>
                                        <td>
                                            <a
                                                class="download-document"
                                                href="https://www.omg.org/spec/XML/1.1/PDF"
                                                data-spec="XML/1.1"
                                                data-label="XML/1.1/PDF"
                                                >XML/1.1/PDF</a
                                            >
                                            <br />
                                        </td>
                                        <td
                                            class="document-number"
                                            title="394051"
                                        >
                                            formal/03-04-01
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </section>

                    <hr class="container”/" />
                </section>

                <section id="spec-versions" class="container">
                    <h2 role="heading" aria-level="1">History</h2>

                    <section class="container" id="spec-versions-formal">
                        <h3 role="heading" aria-level="2">Formal Versions</h3>
                        <div class="table-responsive">
                            <table class="table table-striped" data-sortable>
                                <thead>
                                    <tr>
                                        <th class="col-xs-2">Version</th>
                                        <th class="col-xs-3">Adoption Date</th>
                                        <th class="col-xs-7">URL</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>1.1</td>
                                        <td>April 2003</td>
                                        <td>
                                            <a
                                                href="https://www.omg.org/spec/XML/1.1"
                                                >https://www.omg.org/spec/XML/1.1</a
                                            >
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1.0</td>
                                        <td>November 2002</td>
                                        <td>
                                            <a
                                                href="https://www.omg.org/spec/XML/1.0"
                                                >https://www.omg.org/spec/XML/1.0</a
                                            >
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </section>
                    <hr class="container”/" />
                </section>

                <section
                    id="inventory-links"
                    role="complementary"
                    class="container"
                >
                    <h2 role="heading" aria-level="1">Links</h2>
                    <dl class="dl-horizontal">
                        <dt>This Document:</dt>
                        <dd>
                            <a href="https://www.omg.org/spec/XML/1.1/About-XML"
                                >https://www.omg.org/spec/XML/1.1/About-XML</a
                            >
                        </dd>

                        <dt class="small">RDF</dt>
                        <dd class="small">
                            <a
                                href="https://www.omg.org/spec/XML/1.1/About-XML.rdf"
                                >https://www.omg.org/spec/XML/1.1/About-XML.rdf</a
                            >
                        </dd>

                        <dt class="small">JSON-LD</dt>
                        <dd class="small">
                            <a
                                href="https://www.omg.org/spec/XML/1.1/About-XML.jsonld"
                                >https://www.omg.org/spec/XML/1.1/About-XML.jsonld</a
                            >
                        </dd>

                        <dt>Latest Document:</dt>
                        <dd>
                            <a href="https://www.omg.org/spec/XML"
                                >https://www.omg.org/spec/XML</a
                            >
                        </dd>

                        <dt class="small">RDF</dt>
                        <dd class="small">
                            <a href="https://www.omg.org/spec/XML/About-XML.rdf"
                                >https://www.omg.org/spec/XML/About-XML.rdf</a
                            >
                        </dd>

                        <dt class="small">JSON-LD</dt>
                        <dd class="small">
                            <a
                                href="https://www.omg.org/spec/XML/About-XML.jsonld"
                                >https://www.omg.org/spec/XML/About-XML.jsonld</a
                            >
                        </dd>

                        <dt>Members Only</dt>
                        <dd>
                            <a href="https://www.omg.org/members/spec/XML/1.1"
                                >https://www.omg.org/members/spec/XML/1.1</a
                            >
                        </dd>

                        <!-- Supersedes Version -->
                        <dt>Supersedes:</dt>
                        <dd>
                            <a href="https://www.omg.org/spec/XML/1.1/Beta1"
                                >https://www.omg.org/spec/XML/1.1/Beta1</a
                            >
                        </dd>

                        <!-- keywords -->

                        <!-- contact form -->
                        <dt>Contact:</dt>
                        <dd>
                            <span
                                data-toggle="tooltip"
                                data-placement="right"
                                data-container="body"
                                data-html="true"
                                title="Just send a question about this specification"
                            >
                                <a
                                    href="https://www.omg.org/spec/contact?i=XML/1.1"
                                    >Send a question ⓘ</a
                                >
                            </span>
                        </dd>
                    </dl>
                </section>
            </div>
            <!-- Page Content / End -->
        </div>
        <!-- Main / End -->

        <!-- BODY FOOTER INCLUDE BEGIN -->
        <!-- Footer -->
        <footer class="footer" id="footer">
            <div class="footer-widgets">
                <div class="container">
                    <div class="row">
                        <div class="col-sm-4 col-md-3">
                            <!-- Widget :: Custom Menu -->
                            <div class="widget_nav_menu widget widget__footer">
                                <h3 class="widget-title">Custom Links</h3>
                                <div class="widget-content">
                                    <ul>
                                        <li>
                                            <a
                                                href="//www.omg.org/gettingstarted/bod_public.htm"
                                                >Board of Directors</a
                                            >
                                        </li>
                                        <li>
                                            <a
                                                href="//www.omg.org/legal/index.htm"
                                                >Legal</a
                                            >
                                        </li>
                                        <li>
                                            <a
                                                href="//www.omg.org/about/liaison.htm"
                                                >Liaison Relations</a
                                            >
                                        </li>
                                        <li>
                                            <a
                                                href="//www.omg.org/about/staff.htm"
                                                >Meet Our Staff</a
                                            >
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            <!-- /Widget :: Custom Menu -->
                        </div>
                        <div class="col-sm-4 col-md-6">
                            <!-- Widget :: Text Widget -->
                            <div class="widget_text widget widget__footer">
                                <h3 class="widget-title">About Us</h3>
                                <div class="widget-content">
                                    <p>
                                        The Object Management Group&reg;
                                        (OMG&reg;) is an international, open
                                        membership, not-for-profit technology
                                        standards consortium.
                                    </p>

                                    <p>
                                        Founded in 1989, OMG standards are
                                        driven by vendors, end-users, academic
                                        institutions and government agencies.
                                        OMG Task Forces develop enterprise
                                        integration standards for a wide range
                                        of technologies and an even wider range
                                        of industries.
                                    </p>
                                    <a
                                        href="//www.omg.org/about/index.htm"
                                        class="btn btn-primary"
                                        >Learn More</a
                                    >
                                </div>
                            </div>
                            <!-- /Widget :: Text Widget -->
                        </div>
                        <div class="col-sm-4 col-md-3">
                            <!-- Widget :: Contacts Info -->
                            <div class="contacts-widget widget widget__footer">
                                <h3 class="widget-title">Contact Us</h3>
                                <div class="widget-content">
                                    <ul class="contacts-info-list">
                                        <li>
                                            <i class="fa fa-map-marker"></i>
                                            <div class="info-item">
                                                9C Medway Road, PMB 274<br />
                                                Milford, MA 01757 USA
                                            </div>
                                        </li>
                                        <li>
                                            <i class="fa fa-phone"></i>
                                            <div class="info-item">
                                                Ph.+1 781 444-0404<br />
                                                Fax +1 781-444-0320
                                            </div>
                                        </li>
                                        <li>
                                            <i class="fa fa-envelope"></i>
                                            <span class="info-item">
                                                <a
                                                    href="/cdn-cgi/l/email-protection#f39a9d959cb39c9e94dd9c8194"
                                                    ><span
                                                        class="__cf_email__"
                                                        data-cfemail="9af3f4fcf5daf5f7fdb4f5e8fd"
                                                        >[email&#160;protected]</span
                                                    ></a
                                                >
                                            </span>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            <!-- /Widget :: Contacts Info -->
                        </div>
                    </div>
                </div>
            </div>
            <div class="footer-copyright">
                <div class="container">
                    <div class="row">
                        <div class="col-sm-6 col-md-6">
                            Copyright &copy; 2024
                            <a href="//www.omg.org/index.htm"
                                >Object Management Group&reg;, OMG&reg;</a
                            >
                            &nbsp;| &nbsp;All Rights Reserved
                        </div>
                        <div class="col-sm-6 col-md-6">
                            <div class="social-links-wrapper">
                                <span class="social-links-txt"
                                    >Connect with us</span
                                >
                                <ul class="social-links social-links__dark">
                                    <li>
                                        <a
                                            href="https://www.facebook.com/Object-Management-Group-171534410022/"
                                            ><i class="fa fa-facebook"></i
                                        ></a>
                                    </li>
                                    <li>
                                        <a
                                            href="https://twitter.com/objectmgmtgroup"
                                            ><i class="fa fa-twitter"></i
                                        ></a>
                                    </li>
                                    <li>
                                        <a
                                            href="https://www.linkedin.com/groups/66799"
                                            ><i class="fa fa-linkedin"></i
                                        ></a>
                                    </li>
                                    <li>
                                        <a href="https://blog.omg.org/"
                                            ><i
                                                class="fa fa-pencil-square-o"
                                            ></i
                                        ></a>
                                    </li>
                                    <li>
                                        <a
                                            href="https://www.youtube.com/channel/UCtuTj1wtywojYNZoyPeYAFw"
                                            ><i class="fa fa-youtube"></i
                                        ></a>
                                    </li>
                                    <li>
                                        <a
                                            href="https://plus.google.com/b/112303461995870315156/112303461995870315156/posts"
                                            ><i class="fa fa-google-plus"></i
                                        ></a>
                                    </li>
                                    <li>
                                        <a href="#"
                                            ><i class="fa fa-rss"></i
                                        ></a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        <!-- Footer / End -->

        <!-- Javascript Files
    ================================================== -->
        <script
            data-cfasync="false"
            src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"
        ></script>
        <script src="https://www.omg.org/vendor/jquery-1.11.0.min.js"></script>
        <script src="https://www.omg.org/vendor/jquery-migrate-1.2.1.min.js"></script>
        <script src="https://www.omg.org/vendor/bootstrap.min.js"></script>
        <script src="https://www.omg.org/vendor/headhesive.min.js"></script>
        <script src="https://www.omg.org/vendor/fhmm.js"></script>
        <script src="https://www.omg.org/vendor/jquery.flickrfeed.js"></script>
        <script src="https://www.omg.org/vendor/isotope/isotope.pkgd.min.js"></script>
        <script src="https://www.omg.org/vendor/isotope/jquery.imagesloaded.min.js"></script>
        <script src="https://www.omg.org/vendor/magnific-popup/jquery.magnific-popup.js"></script>
        <script src="https://www.omg.org/vendor/owl-carousel/owl.carousel.min.js"></script>
        <script src="https://www.omg.org/vendor/jquery.fitvids.js"></script>
        <script src="https://www.omg.org/vendor/jquery.appear.js"></script>
        <script src="https://www.omg.org/vendor/jquery.stellar.min.js"></script>
        <script src="https://www.omg.org/vendor/snap.svg-min.js"></script>
        <script src="https://www.omg.org/vendor/mediaelement/mediaelement-and-player.min.js"></script>
        <script
            async=""
            src="https://www.google-analytics.com/ga.js"
            type="text/javascript"
        ></script>

        <script src="https://www.omg.org/js/custom.js"></script>

        <!-- sortable tables -->
        <script src="https://unpkg.com/bootstrap-table@1.18.3/dist/bootstrap-table.min.js"></script>

        <script
            crossorigin="anonymous"
            integrity="sha256-+mWd/G69S4qtgPowSELIeVAv7+FuL871WXaolgXnrwQ="
            src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js"
        ></script>
        <link
            crossorigin="anonymous"
            href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css"
            integrity="sha256-xJOZHfpxLR/uhh1BwYFS5fhmOAdIRQaiOul5F/b7v3s="
            rel="stylesheet"
        />
        <script type="text/javascript">
            $(document).ready(function () {
                const searchBox = $("#specs-search-box");
                searchBox.select2({
                    placeholder:
                        "Type Specifications, Categories, Keywords or Companies",
                    allowClear: true,
                    minimumResultsForSearch: 5,
                });
                searchBox.on("select2:select", function (e) {
                    let path = e.currentTarget.value;
                    searchBox.val([]).trigger("change");
                    if (!window.location.href.endsWith("/")) path = "/" + path;
                    window.location.href = window.location.href + path;
                });
                $("#specs-search-button").hide();
                $("a.download-document").click(function () {
                    gtag("event", "download", {
                        event_category: "downloads",
                        event_action: $(this).data("spec"),
                        event_label: $(this).data("label"),
                    });
                });
            });
            $('[data-toggle="tooltip"]').tooltip();
        </script>
        <!-- BODY FOOTER INCLUDE END -->

        <!-- Start of HubSpot Embed Code -->
        <script
            type="text/javascript"
            id="hs-script-loader"
            async
            defer
            src="//js.hs-scripts.com/22770735.js"
        ></script>
        <!-- End of HubSpot Embed Code -->
    </body>
</html>
```
