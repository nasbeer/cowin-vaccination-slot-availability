import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, table, thead, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      link, a{
        color:#fff;
      }
      footer {visibility: hidden;}
        table {font-family:sans-serif;}
        }
        thead {position:relative;display: table-header-group;
    vertical-align: middle;
    border-color: inherit;}
     .stApp { bottom: 40px; }
     @media only screen and (max-width: 480px) {
        table, thead, tbody{overflow-x:scroll !important;
        max-width:480px;
        }
     }
     css-8xv65a{
     display:none;
     }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        backgroundColor="#333",
        padding=px(10,0,0,0),
        width=percent(100),
        color="#fff",
        text_align="center",
        height="fit-content",
        opacity=1
    )
    style_table = styles(
        backgroundColor="#09c"
    )


    body = p()
    foot = div(
        style=style_div
    )(
        body
    )
    thead = table(
        style=style_table
    )


    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)
    st.markdown(str(thead), unsafe_allow_html=True)


def footer(inp_views):
    myargs = [

        "Page Visits - ", str(inp_views),
        br(),
        "&copy; 2021 | All Rights Reserved | Created by ",
        link("https://nasbeer.com", "<span style='color:#fff;text-decoration:none;'>Nasbeer Ahammed</span>"),
        "     ",
        
    ]
    layout(*myargs)
