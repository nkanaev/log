---
name: Brief history of CSS colors
tags: [web, unix]
---

I've decided to create a personal blog. After a few hours of searching for a perfect template, I went with [Rosa theme][rosa-theme]. The only thing I changed (apart from minor cosmetic HTML tweaks) was the link color. I set it to `steelblue`, which is visible when you hover over a link. I don't have time for choosing the perfect color, because I have more important things to spend my time on. 

[rosa-theme]: https://github.com/davidmerfield/Blot/tree/d31f2f8c/app/templates/latest/rosa

Which is - finding out where did `steelblue` color come from to CSS. The search of color origins revealed a lot of interesting backstory, forgotten memes and even a tragic loss of the people behind the computing history. 

# History of colors in CSS

In early 90's Tim Berners-Lee publishes the first prototype of what would become WWW. Internet becomes a new hot thing, HTML becomes the language of the Web, and in 1994 Tim Berners-Lee founds W3C - organization behind standardization of the Web.

People start building websites, and one of the most requested features is document customization. Web developers want to be able to layout and add colors to their HTML. So CSS1 recommendation came in 1996 to address this. It specifies a lot of niceties, among which is ability to [set colors][css1-colors], both using RGB codes and keywords. Color name keywords were taken from [MS Windows 16 color palette][mswin-colors]. `orange` was [added][css2-orange] later on to CSS2.

CSS3 came around not long after. For the reasons unknown to me, 2001 draft spec added [even more color keywords][css3-colors], this time from X11 (windowing system for Unix-like operating systems). It had a fair amount of [criticism][css3-colors-criticism], but ends up in a spec anyways. This spec mentions `steelblue` for the first time.

In 2014 `rebeccapurple` [was proposed][rebeccapurple-proposal] and added to CSS4 spec, [in memoriam][rebecca-memoriam] of Eric A. Meyer's daughter Rebecca, the man who played major role in CSS advocacy.

[css1-colors]: https://www.w3.org/TR/REC-CSS1/#color-units
[css2-orange]: https://www.w3.org/TR/CSS2/changes.html#q21.2
[mswin-colors]: https://en.wikipedia.org/wiki/List_of_software_palettes#Microsoft_Windows_default_16-color_palette
[css3-colors]: https://www.w3.org/TR/2001/WD-css3-color-20010305#x11-color
[css3-colors-criticism]: https://lists.w3.org/Archives/Public/www-style/2002May/0122.html
[rebeccapurple-proposal]: https://lists.w3.org/Archives/Public/www-style/2014Jun/0257.html
[rebecca-memoriam]: http://meyerweb.com/eric/thoughts/2014/06/09/in-memoriam-2/

# History of colors in X11

So `steelblue` came from X11, it turns out. And to answer the initial question we need to go further back in history.

Xerox releases Alto in 1973 - the first computer with what would become today's GUI. During late 70's and early 80's GUI becomes a new hot thing. Microsoft and Apple present operating systems which offer GUIs.

In the meantime enthusiasts from MIT come up with X Window System in 1984. The next year X adds color support. Jim Gettys [creates][rgbtxt-jg] a list of color names, with "steelblue" among them.

Paul Raveling [updates the list][rgbtxt-pr] in 1989. Being a software engineer with a total lack of control, he ends up adding a bunch of new colors (`dodgerblue`?), changing the existing ones during the course. This update, which includes final "tuned" version of `steelblue`, ends up in CSS spec along with others' [contributions][css3-colors-origin].

<span style="color: steelblue">The End.</span>

[css3-colors-origin]: https://lists.w3.org/Archives/Public/www-style/2014Mar/0272.html
[rgbtxt-jg]: https://cgit.freedesktop.org/~alanc/xc-historical/commit/xc/programs/rgb/rgb.txt?id=0d0ad63237618270e48503a37ce542139d7abab5
[rgbtxt-pr]: https://cgit.freedesktop.org/~alanc/xc-historical/commit/xc/programs/rgb/rgb.txt?id=6904446b8a8dc2bdf6f420f5436552ee920d70e2
