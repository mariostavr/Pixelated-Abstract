import matplotlib as mpl
import matplotlib.pyplot as plt
import os
from shutil import move

#========================= FUNCTION - EXECUTE =========================
def plot_all_cmaps(names):

    rows, cols = 13, 13     #Figure
    height, width = 7, 14   #Color Box

    cmap_ids = plt.colormaps()
    n_cmaps = len(cmap_ids)
    
    index = 0

    fig, axes = plt.subplots(rows, cols, figsize=(width, height))
    fig.suptitle('Palette', fontsize=25)

    while index < n_cmaps:
        for row in range(rows):
            for col in range(cols):
                ax = axes[row, col]
                cmap_id = cmap_ids[index]
                clr_names.append(cmap_id)   #List
                cmap = plt.get_cmap(cmap_id)
                mpl.colorbar.ColorbarBase(ax, cmap=cmap,orientation='horizontal')
                ax.set_title(f"{cmap_id}", fontsize=8)
                ax.tick_params(left=False, right=False, labelleft=False,labelbottom=False, bottom=False)


                last_iteration = index == n_cmaps-1
                if (row==rows-1 and col==cols-1) or last_iteration:
                    plt.tight_layout()
                    plt.savefig('Palette.png')
                    if last_iteration: return
                index += 1
#======================================================================


#--------------------------Main
clr_names = []
plot_all_cmaps(clr_names)



#move('Palette.png', 'Palette.gif')
plt.close()