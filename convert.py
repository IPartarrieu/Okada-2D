import meshio

prefix="vankeken14"       # Esto hay que cambiarlo en cada caso
dim   = 2              # Esto hay que cambiarlo en cada caso

# De aqui hacia abajo NO TOCAR!!
msh = meshio.read(prefix+".msh")

def create_mesh(mesh, cell_type, outname, prune_z=False):
    cells = mesh.get_cells_type(cell_type)
    cell_data = mesh.get_cell_data("gmsh:physical", cell_type)
    points = mesh.points[:,:2] if prune_z else mesh.points
    out_mesh = meshio.Mesh(points=points, cells={cell_type: cells}, cell_data={outname:[cell_data]})
    return out_mesh

if dim==2:

    # Create and save one file for the mesh, and one file for the facets 
    triangle_mesh = create_mesh(msh, "triangle", "subdomains",prune_z=True)
    line_mesh     = create_mesh(msh, "line", "boundaries",prune_z=True)

    meshio.write(prefix+"_domain.xdmf", triangle_mesh)
    meshio.write(prefix+"_boundaries.xdmf", line_mesh)

else:

    tetra_mesh    = create_mesh(msh, "tetra","subdomains",prune_z=False)
    triangle_mesh = create_mesh(msh, "triangle","boundaries",prune_z=False)
    #
    meshio.write(prefix+"_domain.xdmf", tetra_mesh)
    meshio.write(prefix+"_boundaries.xdmf", triangle_mesh)
    
