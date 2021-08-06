import instaloader as ins
from instaloader import Post

var = ins.Instaloader()

var.login("", "")  # (login)
var.interactive_login("")      # (ask password on terminal)
var.load_session_from_file("")
# (load session created w/ `instaloader -l USERNAME`)

post = Post.from_shortcode(var.context, "CQ36GDmNTKX")