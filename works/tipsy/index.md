---
name: tipsy
desc: software renderer
---

_tipsy_ is a PS1-like software renderer.

<video src="promo.mp4" autoplay muted loop></video>

The name has a double meaning: it's short for "**ti**ny **P**lay**S**tation**y**",
but it also characterises the console's peculiar graphics.

The project is written in ~500 lines of C99. This includes
a parser for a subset of Wavefront .obj file format,
functions for vector operations and a graphics rasterizer.
The rest (basic drawing helpers, mouse/keyboard input, PNG reader)
is handled by Erik Agsjö [magnificent little library][tigr].

Source code: https://github.com/nkanaev/tipsy

[tigr]: https://github.com/erkkah/tigr
