#!/usr/bin/env python3
"""Builds the portfolio site. Content mirrors the PDF portfolio exactly:
each project keeps its own labels, paragraph order and figure count."""

import html, os

NAME = "Fikret Can Ozenli"
ROLE = "Portfolio — Mechanical Engineer · Design, Simulation & Installation"
EMAIL = "fikretcanozenli@gmail.com"
PHONE = "+32 456 73 72 33"
LINKEDIN = "linkedin.com/in/fikret-can-ozenli"

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrap">
"""

FOOT = """
<footer>
{foot}
</footer>
</div>
</body>
</html>
"""

def esc(s):
    return html.escape(s, quote=False)

def field(label, value, link=None, wide=False):
    v = f'<a href="{link}">{esc(value)}</a>' if link else esc(value)
    cls = "field field--wide" if wide else "field"
    return f'<div class="{cls}"><dt>{esc(label)}</dt><dd>{v}</dd></div>'

# ---------------------------------------------------------------------------
# CONTENT
#
# Each project has "blocks": an ordered list of tuples.
#   ("lab",  "Brief", "text")      a bold label followed by text
#   ("p",    "text")               a plain paragraph
#   ("sub",  "Project — name")     a sub-project heading
#   ("bullets", "Key decisions", [ ... ])   heading plus bulleted list
#   ("fig",  "fig08.jpg", "caption")
#   ("video","YOUTUBEID", "caption")
#   ("link", "label", "url")
# ---------------------------------------------------------------------------

PROJECTS = [
{
 "slug":"production-equipment",
 "title":"Battery Production Line Equipment",
 "summary":"Conveyor systems and water cooling for battery test facilities, designed and then installed on customer sites.",
 "tag":"Professional",
 "thumb":"fig01.jpg",
 "fields":[("Employer","Project Engineering & Contracts NV"),
           ("Period","Mar 2024 – Jun 2026"),
           ("Location","Leuven, Belgium"),
           ("Field","Battery production equipment")],
 "blocks":[
   ("p","My work covered the full life of a design rather than a single stage of it: mechanical design of automated line components — principally conveyor solutions and water cooling systems for battery testers — for battery filling, sealing, processing and testing facilities. Because I followed my own designs through to installation, I saw directly which decisions held up and which did not, and that feedback loop changed how I design. It also meant constant contact with other disciplines and with technicians, and dealing with the problems that only surface once equipment meets a real building. The equipment is customer-specific, so I cannot share drawings or project detail, but the images below give a sense of the work."),
   ("fig","fig01.jpg","Figure 1 — From conveyor installation / Automotive battery production facility"),
   ("fig","fig02.jpg","Figure 2 — HVAC cooling system installation for battery testers / Automotive battery production facility"),
 ]},
{
 "slug":"ev-torque-controller",
 "title":"AI Controller for EV Torque Transition",
 "summary":"Replacing hand-calibrated torque maps with a reinforcement learning agent, validated by co-simulation.",
 "tag":"Controls",
 "thumb":"fig03.jpg",
 "fields":[("Employer","Toyota Motor Europe"),
           ("Period","Jul 2023 – Jan 2024"),
           ("Location","Brussels, Belgium"),
           ("Field","Electric vehicle driveability")],
 "blocks":[
   ("p","Through this internship I had the chance to join the Powertrain department in Toyota Motor Europe at the Toyota Technical Centre R&D facility based in Zaventem, Belgium. A research-focused role on the control side rather than the mechanical side. I worked on smoothing torque transition in electric vehicles — developing and testing an AI controller in MATLAB and Simcenter AMESim, and using real track test data to refine both the model and the control strategy iteratively."),
   ("p","Key skills gained were control theory, data analysis, AI and simulation experience especially in vehicle dynamics and frequency response. Due to confidentiality reasons, I am limited in details I can give."),
   ("sub","Project — AI controller for EV torque transition"),
   ("lab","Problem","The torque smoothening was carried out by many hard coded maps calibrated by lots of tests in extensive processes."),
   ("lab","Approach","To replace the hard coded maps with Reinforcement Learning agent that can learn the torque transition by repeated simulation training simplifying the control logic."),
   ("lab","Validation","Used AMESim (Vehicle model) – MATLAB (RL Agent) models to co-simulate the two and validate the response of the vehicle in terms of driveability and vehicle dynamics."),
   ("lab","Outcome","I proved the concept that the RL Agent was able to learn and smooth the torque transition. It was also compatible to the control logic for the specific vehicle model. Moreover, a reward function was also developed that was adjustable between different drive modes. However, due to lack of testing time, it was not implemented in physical testing. The results were based purely on the vehicle model, which has its own accuracy limitations."),
   ("fig","fig03.jpg","Figure 3 — Toyota bZ4X was the vehicle I worked on."),
 ]},
{
 "slug":"topology-optimisation",
 "title":"FEA / Topology Optimisation Routine",
 "summary":"An APDL routine that iteratively removes unstressed material from a component while preserving load paths.",
 "tag":"Simulation",
 "thumb":"fig04.jpg",
 "fields":[("Employer","FEM Expert"),
           ("Period","May 2022 – Sep 2022"),
           ("Location","Madrid, Spain"),
           ("Field","FEA and structural analysis")],
 "blocks":[
   ("p","My first engineering role, focused on simulation. Day to day I ran FEA analyses of components in ANSYS APDL, contributing to design stability assessments and topology optimisation studies. It was where I learned to work analytically. I learnt to set a problem up carefully, question the results, and understand what the model was and was not telling me."),
   ("sub","Project 1 — FEA / Topology optimisation routine"),
   ("lab","Problem","Some components designed for specific loads and use cases are inefficient in weight, cost and material use because they are excessively bulky. FEA is an efficient tool to visualize the stress distribution and detect parts of the components which are basically “unused”, however to run separate simulations and redefining geometry of parts at every iteration is a complex and time consuming task."),
   ("lab","Approach","Using APDL language in ANSYS Mechanical, I wrote a routine that automates the process, running iterative simulations and modifications on the part design. The general principle was to calculate the stress levels on each element and remove low stress parts and redo the analysis until desired material loss was achieved."),
   ("lab","Outcome","I created an automated script that can be used in different scenarios and different components. Below is one of my test cases (actual component simulations cannot be shared): a flat plate supported at the top and bottom left corners, loaded at the top right corner."),
   ("fig","fig04.jpg","Figure 4 — FEA topology optimization"),
   ("video","xJjLbbNX204","The full simulation"),
 ]},
{
 "slug":"neural-network-stiffness",
 "title":"Neural Network for Joint Stiffness Prediction",
 "summary":"Predicting the stiffness of complex tubular joints from their force–deflection response, using a network built from scratch in Python.",
 "tag":"Research",
 "thumb":"fig05.jpg",
 "fields":[("Employer","FEM Expert"),
           ("Period","May 2022 – Sep 2022"),
           ("Location","Madrid, Spain"),
           ("Dataset","~100,000 FEA simulations")],
 "blocks":[
   ("sub","Project 2 — Neural network for joint stiffness prediction"),
   ("lab","Problem","A proof-of-concept study alongside senior engineers, predicting the stiffness of complex mechanical joints from their force–deflection response using a neural network trained on roughly 100,000 FEA simulations. Beam elements are widely used for tubular structures because they are computationally cheap, but their simplified formulation reduces two different junction geometries to the same representation:"),
   ("fig","fig05.jpg","Figure 5 — Two different junction geometries reduced to the same beam representation"),
   ("p","To resolve this while keeping the efficiency of beam elements, a novel joint was devised: a junction built from six zero-length elements defining its stiffness in six degrees of freedom. The goal was to determine whether those stiffness values could be predicted by a neural network, using the force and deviation matrices as input — a proof of concept for ANN–FEM cooperation."),
   ("fig","fig06.jpg","Figure 6 — Novel junction built from six zero-length elements"),
   ("lab","Approach","I had almost no machine learning background at the time — one semester of coursework — and deliberately chose not to use ready-made libraries such as Keras or PyTorch. I did not want a black box; I wanted to understand how the method actually worked, so I built the entire network from scratch in raw Python. It took about a week and a half, and it worked. What I take from it is less the result than the approach: I chose the harder path in order to understand something properly, and taught myself a difficult subject quickly from first principles."),
   ("lab","Outcome","The published paper can be read here:"),
   ("link","Read the published paper","https://www.mdpi.com/2227-7390/11/15/3261"),
   ("fig","fig07.jpg","Figure 7 — Training Dataset MSE vs Validation Dataset MSE"),
 ]},
{
 "slug":"gnss-mast",
 "title":"GNSS Base Station — 6 m Deployable Mast",
 "summary":"A 6 m mast under 40 kg that assembles by hand without tools and packs into a pickup bed.",
 "tag":"Structure",
 "thumb":"fig08.jpg",
 "fields":[("Type","Self-directed design concept"),
           ("Material","6061 aluminium, anodised"),
           ("Tools","Autodesk Inventor, MATLAB"),
           ("Constraints","6 m deployed · under 40 kg · tool-free")],
 "blocks":[
   ("lab","Brief","Design concept for a portable GNSS base station mast: 6 m deployed height, under 40 kg, tool-free hand installation, protection against moisture, dust and dirt, suitable for rugged outdoor use, and packable into the bed of a pickup truck."),
   ("lab","Approach","The approach taken was to build a retractable mast with rails to compress from 6 m to 1.5 m. The design combines welded components, laser-cut platework and standard off-the-shelf parts. Taking inspiration from tripod GNSS bases."),
   ("p","The structure consists of 4 triangular-prism like trusses scaled down to a smaller size nested with a concentric radii. Each level contains the same elements where the bottom and top triangles are formed by hollow aluminium tubes connected by middle pieces and 60° welded corner nodes. The top and bottom triangles are connected to each other via vertical base plates screwed onto the middle pieces."),
   ("bullets","Key decisions",[
     "Material: 6061 aluminium, anodised. The members are extruded hollow tube, which rules out 5052 (poor extrudability); 6061 extrudes, welds, threads and anodises well, satisfying all four constraints at once.",
     "Corner nodes: welded from two angle-cut tube stubs rather than machined from billet. The nodes must be hollow to meet the weight target, which makes billet machining impractical, and casting is not justified at this volume.",
     "Connections: threaded tube-to-node joints, chosen over a slip fit for positive resistance to pull-out under wind and self-weight loading.",
     "Environmental protection: right-sized to the requirement. The structural joints are not pressurised, so corrosion protection via a shedding cover was specified rather than a leak-tight seal.",
     "A MATLAB script was used to calculate the distance between the two concentric triangle sides and length of each side at every level.",
   ]),
   ("fig","fig08.jpg","Figure 8 — Compressed and extended views"),
   ("fig","fig09.jpg","Figure 9 — First level"),
   ("parts",[
     ("Linear guide rail PS 4-20 — ITEM", "https://www.item24.com/en-be/linear-guide-rail-ps-4-20-67553"),
     ("Adjustable foot 80x40 M12x120 — ITEM", "https://www.item24.com/en-at/adjustable-foot-80x40-m12x120-60893?thread=12&adjustingRange=37"),
   ]),
   ("fig","fig10.jpg","Figure 10 — Interface between levels"),
   ("parts",[
     ("Snap door lock BMSVL, lever release — Elesa+Ganter", "https://www.elesa-ganter.com/en/www/latches--snap-door-lock--bmsvl"),
     ("Snap door lock BMS, simpler version — Elesa+Ganter", "https://www.elesa-ganter.com/en/www/latches--snap-door-lock--bms"),
     ("Bearing carriage PS 4-20 — ITEM", "https://www.item24.com/en-it/bearing-carriage-ps-4-20-66639?numberBearings=4&railWidthList=20"),
   ], 3),
   ("fig","fig11.jpg","Figure 11 — MATLAB script to calculate side lengths"),
 ]},
{
 "slug":"snap-lock",
 "title":"Push-to-Release Snap Lock — Mechanism Design",
 "summary":"A latch holding tension that releases consistently regardless of applied load, using an out-of-plane release path.",
 "tag":"Mechanism",
 "thumb":"fig12.jpg",
 "fields":[("Type","Self-initiated mechanism study"),
           ("Materials","MJF PA12, steel"),
           ("Tools","Autodesk Inventor"),
           ("Scope","Concept to manufacture")],
 "blocks":[
   ("lab","Brief","Self-initiated project to develop mechanism design skills. Objective: a compact push-to-lock, push-to-release latch that holds tension securely and releases consistently regardless of the load applied to it."),
   ("lab","Approach","An arrowhead pin enters a frame and spreads two spring-loaded pawls, which return behind the barb to lock. Release is achieved by displacing the pawls out of the locking plane rather than spreading them, so the release path is independent of the direction of applied load."),
   ("bullets","Key decisions",[
     "Out-of-plane release: chosen over a spreading release so that tension on the latch cannot contribute to unlatching, and so release force does not vary with applied load.",
     "Return springs: compression springs seated on captive posts rather than torsion springs — simpler to locate, more forgiving on tolerances, and available from stock rather than custom.",
     "Spring selection: sized from the required holding force and the travel at full pawl opening, with preload set so the pawls are held firmly closed at rest, and solid height checked against the geometric hard stop.",
     "Insertion geometry: 45° ramp on the arrowhead, checked against the friction angle to confirm the wedge cannot self-lock, with the friction penalty accounted for when sizing the springs.",
     "Manufacture: MJF-printed PA12 frame and pawls with heat-set threaded inserts, and steel for the arrowhead and pivot pins where wear and contact stress concentrate. Using MJF printing reduces the cost and weight substantially while keeping the loaded interfaces in metal to have higher durability and resistance to wear.",
     "Self-criticism: As a self-initiated learning project, I did not design any mounting interface into the casing so the lock does not fasten anything to anything else — it only latches to itself.",
   ]),
   ("fig","fig12.jpg","Figure 12 — Completed view on LHS, top casing invisible on RHS."),
   ("bullets",None,[
     "The bottom counterpart was initially a single machined part. To improve manufacturability and reduce cost, I switched to a screwed assembly of an MJF-printed base and a steel arrowhead pin.",
   ]),
   ("fig","fig13.jpg","Figure 13 — Snap lock bottom counterpart."),
   ("fig","fig14.jpg","Figure 14 — Locked form on LHS, pressed to release form on RHS."),
 ]},
{
 "slug":"push-push-latch",
 "title":"Push-Push Latch — Mechanism Design",
 "summary":"A latch that locks on the first push and releases on the second, developed from first principles rather than copied.",
 "tag":"Mechanism",
 "thumb":"fig16.jpg",
 "fields":[("Type","Self-initiated mechanism study"),
           ("Materials","MJF PA12, steel, stainless sheet"),
           ("Tools","Autodesk Inventor"),
           ("Scope","Concept to manufacture")],
 "blocks":[
   ("lab","Brief","Self-initiated mechanism study. Push-push latches are familiar from pens and cabinet catches, but the internal principle varies considerably between designs. The objective was to develop my own working principle rather than reproduce an existing one: a latch that locks on the first push and releases on the second, returning under its own spring force."),
   ("lab","Approach","A plunger slides axially in a groove, carrying a front ramp, a rear ramp and a slot in its underside. Beneath it sits a spring-loaded pin — the stroke pawn — held in a reciprocating pin housing that can only move perpendicular to the plunger’s axis. A spring-loaded return piece shares the plunger’s groove at the far end of its travel."),
   ("p","On the first push, the plunger’s front ramp meets the stroke pawn’s chamfer and drives it down into its pit. Once the ramp has passed, the pawn springs back up into the plunger’s slot, blocking its return. Pushing further brings the plunger’s rear ramp against the housing’s ramp, driving the housing perpendicular to the plunger’s axis so the pawn slides out from under it and the latch releases. The pawn rises to its full height, where the plunger’s side wall prevents it dropping back into the slot. Meanwhile the plunger has compressed the return piece, which drives it back out once the pushing force is released. As the plunger withdraws, the housing returns to its rest position and places the pawn back in the plunger’s path."),
   ("bullets","Key decisions",[
     "Stroke pawn geometry was the hardest part of the design, because four requirements are coupled. The pawn must protrude far enough above the plunger’s slot to latch with margin; compress far enough for the plunger to pass over it; retain enough engagement depth in its bore to resist bending and tilting under the plunger’s side load; and leave room beneath it for a spring capable of delivering the return force. Changing any one of the slot depth, pawn height, bore depth or spring free length moves all the others, so the arrangement had to be resolved as a system rather than feature by feature.",
     "Sliding interfaces drove the material split. A stainless sheet is let into the casing floor so the housing runs on metal rather than PA12 against PA12, which has the widest friction spread and the worst tendency to stick-slip of the available pairings. The stroke pawn is steel, both because its tip takes repeated ramp impact and because steel in a PA12 bore is the best-behaved sliding fit available.",
     "Insertion and release forces were sized from the spring rates and ramp geometry, using the wedge relationship to account for friction at the ramps and in the plunger’s groove. Ramp angles were checked against the friction angle to confirm the wedge cannot self-lock.",
   ]),
   ("fig","fig15.jpg","Figure 15 — Push-push latch"),
   ("fig","fig16.jpg","Figure 16 — Internal arrangement with top casing hidden"),
   ("video","zt_VwRItey8","Mechanism's working principle"),
   ("fig","fig17.jpg","Figure 17 — Half section views"),
 ]},
{
 "slug":"phone-stand",
 "title":"Adjustable Phone Stand",
 "summary":"Holding a phone upright while it charges, with independent adjustment of incline and orientation.",
 "tag":"Mechanism",
 "thumb":"fig18.jpg",
 "fields":[("Type","Self-initiated design"),
           ("Materials","MJF PA12, stainless fasteners"),
           ("Tools","Autodesk Inventor"),
           ("Scope","Concept to manufacture")],
 "blocks":[
   ("lab","Brief","A personal problem rather than an abstract exercise: holding a phone upright during calls while it is charging. Leaning it against a surface fails when a cable protrudes from the bottom, and propping it on a desk blocks the monitor behind. The requirement was a stand that holds the phone clear of the surface with the cable free below it, with independent adjustment of both incline and orientation so it can be used in portrait or landscape."),
   ("lab","Approach","Two friction clamps on perpendicular axes, each governing one adjustment."),
   ("p","Incline is set at the base. The base carries a clevis, and the intermediate part’s lower cylinder sits between its lugs. Tightening the knob on the incline pin draws the lugs together onto that cylinder, clamping it and holding the angle of tilt. The lugs raise the pivot above the base platform so the cylinder can rotate without fouling it."),
   ("p","Orientation is set at the top of the intermediate part. Its upper cylinder houses a rotation disc, which carries the holder case on its far face. Tightening the knob on the orientation pin pulls the disc against the cylinder’s back wall, clamping it and holding the phone in portrait or landscape. Because the two axes are perpendicular and the joints are independent, either can be adjusted without disturbing the other."),
   ("bullets","Key decisions",[
     "A pin cannot block rotation about its own axis. The locking element has to be concentric with the pivot for the holes to align at every angle, which rules out pinning and forces a friction clamp at both joints — the mating faces are drawn together and friction across them holds the position.",
     "The rotation disc’s form follows the assembly sequence. It is two discs joined by a pair of narrow webs rather than a solid cylinder. The orientation pin threads into the near disc, and a retaining nut must be fitted behind it so the pin cannot withdraw — but once the disc is inside the housing, that space is unreachable. The webs leave two side openings so the nut can be fitted before the disc is installed. The part is shaped by the order in which it has to be built.",
     "The incline pin’s length was set by the release condition, not the clamped one. It has to be long enough that when the knob is backed off, the retaining nut does not bottom against the outer face of the far lug before the clamp has released, or the joint would never turn freely.",
     "Fastening. A captured DIN 934 nut sits in an interference-fit hexagonal recess in the base lug, recessed below the surface so it becomes permanent once assembled. The rotation disc uses M5 heat-set inserts. The holder case screw sits in a counterbore so its head cannot bear against the back of the phone.",
     "The holder case holds the phone on six tabs, two at the bottom and two on each side, with a gap between the lower tabs for the charging cable. Cutouts on the sides, top and bottom reduce material and cost.",
   ]),
   ("fig","fig18.jpg","Figure 18 — Complete assembly, with phone"),
   ("fig","fig19.jpg","Figure 19 — Rotation disc design"),
   ("fig","fig20.jpg","Figure 20 — Incline adjustment"),
   ("fig","fig21.jpg","Figure 21 — Orientation adjustment"),
 ]},
]

# ---------------------------------------------------------------------------

def render_blocks(blocks):
    out = []
    for blk in blocks:
        kind = blk[0]
        if kind == "p":
            out.append(f"<p>{esc(blk[1])}</p>")
        elif kind == "lab":
            out.append(f'<p><b class="lab">{esc(blk[1])}</b> {esc(blk[2])}</p>')
        elif kind == "sub":
            out.append(f'<h2 class="sub">{esc(blk[1])}</h2>')
        elif kind == "bullets":
            if blk[1]:
                out.append(f'<p class="bulhead">{esc(blk[1])}</p>')
            out.append("<ul class=\"bul\">")
            for item in blk[2]:
                out.append(f"  <li>{esc(item)}</li>")
            out.append("</ul>")
        elif kind == "fig":
            out.append(
                f'<figure>\n  <img src="images/{blk[1]}" alt="{esc(blk[2])}">\n'
                f'  <figcaption>{esc(blk[2])}</figcaption>\n</figure>')
        elif kind == "video":
            out.append(
                '<figure>\n  <div class="video">\n'
                f'    <iframe src="https://www.youtube.com/embed/{blk[1]}" '
                f'title="{esc(blk[2])}" loading="lazy" allowfullscreen '
                'allow="accelerometer; clipboard-write; encrypted-media; picture-in-picture"></iframe>\n'
                f'  </div>\n  <figcaption>{esc(blk[2])}</figcaption>\n</figure>')
        elif kind == "link":
            out.append(f'<p><a href="{blk[2]}">{esc(blk[1])}</a></p>')
        elif kind == "parts":
            start = blk[2] if len(blk) > 2 else 1
            out.append(f'<ol class="parts" start="{start}" style="counter-reset: part {start - 1}">')
            for label, url in blk[1]:
                out.append(f'  <li><a href="{url}" target="_blank" rel="noopener">{esc(label)}</a></li>')
            out.append("</ol>")
    return "\n".join(out)


def build_index():
    fields = "".join([
        field("Discipline", "Mechanical design"),
        field("Location", "Leuven, Belgium"),
        field("Email", EMAIL, "mailto:" + EMAIL, wide=True),
        field("Phone", PHONE),
        field("LinkedIn", "Profile", "https://www." + LINKEDIN),
    ])
    rows = []
    for p in PROJECTS:
        rows.append(f"""    <li class="sheet">
      <a href="{p['slug']}.html">
        <img class="thumb" src="images/{p['thumb']}" alt="">
        <span class="meat">
          <h2>{esc(p['title'])}</h2>
          <p>{esc(p['summary'])}</p>
        </span>
        <span class="tag">{esc(p['tag'])}</span>
      </a>
    </li>""")
    body = f"""<header class="titleblock">
  <h1>{esc(NAME)}</h1>
  <p class="role">{esc(ROLE)}</p>
  <dl class="fields">
{fields}
  </dl>
</header>

<p class="index-head">Projects</p>
<ul class="sheets">
{chr(10).join(rows)}
</ul>
"""
    return (HEAD.format(title=f"{NAME} — Portfolio",
                        desc="Mechanical engineering portfolio: mechanisms, structures, simulation and production equipment.")
            + body + FOOT.format(foot=f"{esc(EMAIL)} &nbsp;·&nbsp; {esc(PHONE)}"))


def build_project(p):
    fields = "".join(field(k, v) for k, v in p["fields"])
    body = f"""<a class="back" href="index.html">Back to all projects</a>

<header class="proj-head">
  <h1>{esc(p['title'])}</h1>
  <dl class="fields">
{fields}
  </dl>
</header>

{render_blocks(p['blocks'])}
"""
    return (HEAD.format(title=f"{p['title']} — {NAME}", desc=p["summary"])
            + body
            + FOOT.format(foot=f'<a href="index.html">All projects</a> &nbsp;·&nbsp; {esc(EMAIL)}'))


def main():
    out = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(build_index())
    for p in PROJECTS:
        open(os.path.join(out, p["slug"] + ".html"), "w", encoding="utf-8").write(build_project(p))
    print("built index.html +", len(PROJECTS), "project pages")

if __name__ == "__main__":
    main()
