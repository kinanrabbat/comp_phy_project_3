= PHY 68/118 - Computational Physics Project 3
Micah Baum, Parker Chandik, Kinan Rabbat, Sam J. Rayev

Hi! Here's a quick readme to describe what the different programs do, as well as some pictures to highlight certain results we found interesting.

*Adjacency data stored via array indexing:*
- `demo.py` was an initial attempt at having a working Metropolis simulation, and we did get it working, but to allow for more diverse lattice types, we moved on to `demo2.py`

*Adjacency data stored in a list of neighbors:*
- `demo2.py` simulates both square and triangular lattices. It can produce plots of initial vs final magnetizations at various temperatures, as well as depictions of the lattices visually if desired.

*Adjacency data stored in an adjacency matrix:*
- `LatticeNeighborsSim.py` was where we tested out use of an adjacency matrix, as well as plotting of the data
- `Square_and_triangle.py` is largely a reimplementation of LatticeNeighborsSim.py, which also enables triangular matrices. There is some functionality for hexagonal matrices in it, but it is not currently complete/functioning as desired.

== Initial and Final Magnetizations at Different Temperatures
#figure(caption: "Square Lattice",
  grid(columns: 2, 
    figure(caption: "Ferromagnetic", numbering: none,
      image("square_reg.png")
    ),
    figure(caption: "Antiferromagnetic", numbering: none,
      image("square_antiferro.png")
    )
  )

)
#v(1em)
#figure(caption: "Square Lattice",
  grid(columns: 2,
    figure(caption: "Ferromagnetic", numbering: none,
      image("triangle_reg.png")
    ),
    figure(caption: "Antiferromagnetic", numbering: none,
      image("triangle_antiferromagnet.png")
    )  
  )
)

== Final Magnetization of Ferromagnets and Antiferromagnets
#figure(caption: "Square Lattice",
  grid(columns: 2,
    figure(caption: "Ferromagnetic", numbering: none,
      image("square_ferro.png")
    ),
    figure(caption: "Antiferromagnetic", numbering: none,
      image("square_anti.png")
    )  
  )
)
#v(1em)
#figure(caption: "Square Lattice",
  grid(columns: 2,
    figure(caption: "Ferromagnetic", numbering: none,
      image("triangle_ferro.png")
    ),
    figure(caption: "Antiferromagnetic", numbering: none,
      image("triangle_anti.png")
    )  
  )
)
