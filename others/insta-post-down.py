import instaloader as ins
from instaloader import Post

var = ins.Instaloader()

var.login("CarlosViniMSouza", "carlinhos2020")  # (login)
var.interactive_login("CarlosViniMSouza")      # (ask password on terminal)
var.load_session_from_file("CarlosViniMSouza")
# (load session created w/ `instaloader -l USERNAME`)

post = Post.from_shortcode(var.context, "CQ36GDmNTKX")