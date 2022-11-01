import os


files = os.listdir("./pics")
# Filtering only the files.
files = [f for f in files if os.path.isfile(
    "./pics/"+f) and f.endswith(".jpg")]

numCols = 6
cols = [[] for _ in range(0, numCols)]
lb = [[] for _ in range(0, numCols)]
col = 0
for f in files:
    num = str(col) + str(len(cols[col]) // 3)
    cols[col].append(
        "      <a class=\"lightbox\" href=\"#lightbox" + num + "\">")
    cols[col].append("          <img src=\"pics/" + f + "\">")
    cols[col].append("      </a>")

    lb[col].append(
        "   <div class=\"lightbox-target\" id=\"lightbox" + num + "\">")
    lb[col].append("        <img src=\"pics/" + f + "\">")
    lb[col].append("        <h2>")
    lb[col].append("            " + f)
    lb[col].append("        </h2>")
    lb[col].append("        <a class=\"lightbox-close\" href=\"#plants\"></a>")
    lb[col].append("    </div>")

    col += 1
    col = col % numCols


print("<!-- Auto-generated Photo Collage picture layout -->")
print("<div>")
print("<div class=\"picrow\">")
for col in cols:
    print(" <div class=\"piccol\">")
    for row in col:
        print(row)
    print(" </div>")

print("</div>")
print("</div>")
print("<!-- end photo collage -->")

print("<!-- photo collage lightboxes -->")
print("<div>")
for col in lb:
    for row in col:
        print(row)
print("</div>")
print("<!-- end photo collage lightboxes -->")
