from bearlibterminal import terminal as blt


align_center = blt.TK_ALIGN_MIDDLE | blt.TK_ALIGN_CENTER
box_whole = 0x2580
box_upper_half = 0x2588
lucynest_L = "\u258F[+]\u2581"
lucynest_T = "\u2594[+]\u2595"
lucynest = lucynest_L + "ucynes" + lucynest_T
lucynest_colored = f"[color=orange]{lucynest}[/color]"
button_colored_fmt = "[color=orange]%s[/color] %s"
