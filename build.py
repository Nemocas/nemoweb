import glob

PAGE_TOP = r"""<html>
<head>
<title>NemoTITLE</title>
<style type="text/css" media="screen">
body, table { font-family: arial, sans-serif; font-size: 16px; line-height:1.4em; }
h1, h2, h3 { font-weight: normal; }
h1 { font-weight: bold; }
h2 { background-color: #eee; color: #444; padding: 0.3em; }
h3 { font-weight: bold; border-bottom: 2px dotted #aaa; }
h4 { color: #777; }
pre { padding-left: 2em; }
#main { padding: 1em; max-width:900px; margin: 0 auto; }
#content { }

.benchmark { border-collapse:collapse; }
.benchmark td, .benchmark th { border:1px solid #ccc; padding:3px 7px 2px 7px; }
.benchmark th { text-align:left; padding-top:5px; padding-bottom:4px; background-color:#eee; color:#000; }
.benchmark tr.alt td { color:#000; background-color:#f8f8f8; }


</style>
</head>

<body>
<div id="main">

<center><img src="Nemologo.jpg" alt="Nemo"></center>
<br/>

MENU

<br/>

<!-- <hr/> -->

<div id="content">
"""

PAGE_BOTTOM = r"""

<hr style="border:0; height:1px; color:#ccc; background-color:#ccc; margin-top:2em;" />

<div style="line-height:1em">
<p><i>TIMESTAMP</i></p>

<p><i>Contact: <a href="mailto:goodwillhart {at_thingy} googlemail dot com">William Hart</a>, <a href="http://groups.google.com/group/nemo-devel?hl=en">nemo-devel mailing list</a>.</i></p>

<p>Logo background due to Giacomo Merculiano.</p>
</div>

</div>
</div>

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-33043533-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>

</body>
</html>
"""

pages = ["index", "news", "features", "benchmarks", "downloads", "development", "authors", "links"]

page_titles = []
page_texts = []

for page in pages:
    text = open(page + ".txt", "r").read()
    title = text[text.find("<h2>")+4 : text.find("</h2>")]
    page_texts.append(text)
    page_titles.append(title)




from time import gmtime, strftime
timestamp = strftime("Last updated: %Y-%m-%d %H:%M:%S GMT", gmtime())


columns = 3
rows = (len(pages) + columns - 1) // columns

for i in range(len(pages)):
    if 0:
        menu = """<table style="margin-left:auto; margin-right:auto; border-collapse:collapse; border:none;"><tr>\n"""

        for j in range(len(pages)):
            if j % rows == 0:
                menu += """<td style="vertical-align:top"><ul>"""
            if i == j:
                menu += """<li>%s</li>\n""" % page_titles[j]
            else:
                menu += """<li><a href="%s.html">%s</a></li>\n""" % (pages[j], page_titles[j])
            if j % rows == rows - 1 or j == len(pages) - 1:
                menu += """</ul></td>"""

        menu += """</table></tr>\n"""
    else:
        menu = """<div style="text-align:center">"""
        for j in range(len(pages)):
            if i == j:
                menu += """ %s """ % page_titles[j]
            else:
                menu += """<a href="%s.html">%s</a> """ % (pages[j], page_titles[j])
            if j < len(pages) - 1:
                menu += " | "
        menu += """</div>"""

    title = page_titles[i]
    if title == "Overview":
        title = ""
    else:
        title = " - " + title

    fp = open(pages[i] + ".html", "w")
    fp.write(PAGE_TOP.replace("TITLE", title).replace("MENU", menu))
    fp.write(page_texts[i])
    fp.write(PAGE_BOTTOM.replace("TIMESTAMP", timestamp))
    fp.close()


