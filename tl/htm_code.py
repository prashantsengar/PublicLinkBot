def get_html(filepath, filename, URL, publicUrl):
    html = """<!DOCTYPE html>
    <head>
        <meta name="referrer" content="always" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- <script data-ad-client="ca-pub-2196928611152991" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script> -->
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <!-- <script type="text/javascript" src="http://gc.kis.v2.scr.kaspersky-labs.com/FD126C42-EBFA-4E12-B309-BB3FDD723AC1/main.js?attr=fJJpgVGgQAyZyaV3nmonnIcizCOKfKt0GvjwRCcUd5l6uro1drZj5QOEQj2d-5duNTXPnsVVNko_NfXTJWNk-pA4L-8SjGs1_hr3cdpUysfaxpnBuG2l5ncrYy51tnvNqX-J4y3iwxaXyD8izm_l3M0fLnIq7Ut742_nTo00o_o" charset="UTF-8"></script><script async src="https://www.googletagmanager.com/gtag/js?id=UA-150899596-1"></script> -->
        <!-- <script> -->
        <!-- // window.dataLayer = window.dataLayer || [];
        // function gtag(){dataLayer.push(arguments);}
        // gtag('js', new Date());

        // gtag('config', 'UA-150899596-1');
        // </script> -->

        <link rel="stylesheet" href="https://cdn.fluidplayer.com/v2/current/fluidplayer.min.css" type="text/css">
        <script src="https://cdn.fluidplayer.com/v2/current/fluidplayer.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
            .container{
                text-align: center;
                margin: 0% auto;
            }
            @media (orientation: landscape) {
                .container{
                    max-width: 750px;
                }
            }
            .main{
                /* border: 1px solid DodgerBlue;  */
                padding: 0px 2%;
            }
            h1{
                margin-top: 5%;
                color: grey;
                width: fit-width;
                word-wrap: break-word;
                line-height: 20px;
            }
            .filename{
                color: DodgerBlue;
                font-size: calc(10px + 1.1vw);
                word-wrap: break-word;
                font-weight: bold;
            }
            #video-fully-responsive{
                width: 100%;
            }
            #vast_video_loading_video-fully-responsive{
                height: 0;
            }
            .btn {
                background-color: DodgerBlue;
                border: none;
                color: white;
                padding: 12px 30px;
                cursor: pointer;
                font-size: 20px;
                margin: 0% auto;
                margin-top: 20px;
                /* margin-bottom: 20px; */
                width: 100%;
            }
            .btn:hover {
                background-color: RoyalBlue;
            }
            .btnn {
                background-color:#f0ad4e;
                border: none;
                color: white;
                padding: 5px;
                cursor: pointer;
                font-size: 15px;
                margin: 0% auto;
                margin-top: 10px;
                margin-bottom: 20px;
                width: 20%;
            }
        </style>
    </head>"""

    html2 = f"""<body>
        <!-- Ads Managed by AdSpyglass.com -->
    <!-- <script type="text/javascript" src="//cdn.o333o.com/asg_embed.js" data-spots="199784" data-tag="asg"></script> -->
    <!-- <script type="text/javascript" src="//goraps.com/tun.php?section=popunder&pt=8&pub=841753&ga=g"></script> -->
        <div class="container">
            <div class="main">
                <!-- <a href="https://www.purevpn.com/order-now.php?aff=41253&amp;a_bid=06e92bba" target="_blank"><img src="//affiliates.purevpn.com/accounts/default1/6hb82wqa2l/06e92bba.jpg" alt="Best VPN Service" title="Best VPN Service" width="100%" height="auto" /></a> -->
                <!-- <h1>Download</h1> -->
                <!-- <script type="text/javascript" src="//uprimp.com/bnr.php?section=mobile&pub=841753&format=300x50&ga=g"></script>
                <noscript><a href="https://yllix.com/publishers/841753" target="_blank"><img src="//ylx-aff.advertica-cdn.com/pub_2hpya3.png" style="border:none;margin:0;padding:0;vertical-align:baseline;" /></a></noscript> -->

                <p class="filename">{filename}</p>
                <div id='vidiv'>
        <video id="video-fully-responsive" controls >
            <source src={URL} type="video/mp4">
        </video>
        <script type="text/javascript">
            var video = document.querySelector("video");
            var src = video.firstElementChild

            src.addEventListener('error', function(evt) {{
                // video.addEventListener('play', function(evt) {{
                //     document.getElementById('vidiv').style.display = 'none';
                // }})
                document.getElementById('vidiv').style.display = 'none';
            }}); 
            var testVideo = fluidPlayer(
                "video-fully-responsive",
                '',
                {{
                    responsive: true,
                }}
            );
        </script>

        <!-- <video id='dash-video'>
            <source src={publicUrl}/{filepath}/{filename} type='application/dash+xml'/>
        </video>
        
        <script>
        fluidPlayer(
            'dash-video',
            {{
                layoutControls: {{
                    fillToContainer: true
                }}
            }}
        );
        </script> -->

        <!-- <script>
            window.asgvastcnf_overlay = {{
            spotUrl: "//a.o333o.com/api/spots/189996",
            attachTo: "#video-fully-responsive"
            }}
        </script>
        <script type="text/javascript" src="//cdn.o333o.com/vast-im.js"></script> -->
    </div>
                <a href={publicUrl}/{filepath}/{filename}>
                <button class="btn"><i class="fa fa-download"></i> Download</button>
                </a>
                <a href="mailto:prashantsgig@gmail.com?subject=Report for File ID {filepath}/{filename}" target="_blank" style="text-decoration: none;">
                    <button class="btnn">Report</button>
                </a>
            </div>
        </div>
        <!-- <div class="ads" style="text-align: center;">
            

                <script type="text/javascript" src="//uprimp.com/bnr.php?section=main1&pub=841753&format=300x250&ga=g"></script>
                <noscript><a href="https://yllix.com/publishers/841753" target="_blank"><img src="//ylx-aff.advertica-cdn.com/pub/300x250.png" style="border:none;margin:0;padding:0;vertical-align:baseline;" /></a></noscript>
                Ads Managed by AdSpyglass.com
                <iframe class="na" frameborder="0" scrolling="no" width="300" height="250" src="//a.o333o.com/api/spots/195629?p=1"></iframe> -->
                <!-- <script type="text/javascript" src="//uprimp.com/bnr.php?section=main2&pub=841753&format=300x250&ga=g"></script>
                <noscript><a href="https://yllix.com/publishers/841753" target="_blank"><img src="//ylx-aff.advertica-cdn.com/pub/300x250.png" style="border:none;margin:0;padding:0;vertical-align:baseline;" /></a></noscript>
                <script type="text/javascript" src="//uprimp.com/bnr.php?section=main3&pub=841753&format=300x250&ga=g"></script>
                <noscript><a href="https://yllix.com/publishers/841753" target="_blank"><img src="//ylx-aff.advertica-cdn.com/pub/300x250.png" style="border:none;margin:0;padding:0;vertical-align:baseline;" /></a></noscript> -->
                <!-- <a href="https://www.purevpn.com?aff=41253&amp;a_bid=34901b08" target="_top"><img src="//affiliates.purevpn.com/accounts/default1/6hb82wqa2l/34901b08.png" alt="" title="" width="300" height="250" /></a> -->
                
        
            <!-- </div>     -->
    </body>
    """
    htm = html+html2
    return htm


if __name__=='__main__':
    filename = 'filename'
    filepath='filepath'
    URL = 'url'
    publicUrl = 'k.com'
    print(html2)