function swapLinks(clicked) {
   const links = document.getElementById("links");
   links.innerHTML = generateDivElements(clicked);
}

function generateDivElements(clicked) {
    //Outer container to use to set innerHTML
    const linkContainer = document.createElement("div")
    linkContainer.classList.add("link-container")

    //Links container
    const sidebarLinks = document.createElement("div");
    sidebarLinks.classList.add("sidebar-links");

    // The five links here
    const act = document.createElement("div");
    act.classList.add("active");
    const inactive1 = document.createElement("div");
    inactive1.classList.add("inactive");
    const inactive2 = document.createElement("div");
    inactive2.classList.add("inactive");
    const inactive3 = document.createElement("div");
    inactive3.classList.add("inactive");
    const inactive4 = document.createElement("div");
    inactive4.classList.add("inactive");

    // Create the fancy arrows.
    const arrow1 = document.createElement("i");
    arrow1.classList.add("fas");
    arrow1.classList.add("fa-caret-right");
    const arrow2 = document.createElement("i");
    arrow2.classList.add("fas");
    arrow2.classList.add("fa-caret-right")
    const arrow3 = document.createElement("i");
    arrow3.classList.add("fas");
    arrow3.classList.add("fa-caret-right");
    const arrow4 = document.createElement("i");
    arrow4.classList.add("fas");
    arrow4.classList.add("fa-caret-right")
    const arrow5 = document.createElement("i");
    arrow5.classList.add("fas");
    arrow5.classList.add("fa-caret-right");

    // Create the actual text contents
    const home = document.createElement("div");
    home.classList.add("bp-text");
    home.textContent = "Home";
    home.setAttribute('onclick', "swapLinks('Home')");
    home.style.marginLeft = '16px';
    const about = document.createElement("div");
    about.classList.add("bp-text");
    about.textContent = "About";
    about.setAttribute('onclick', "swapLinks('About')");
    about.style.marginLeft = '16px';
    const p1 = document.createElement("div");
    p1.classList.add("bp-text");
    p1.textContent = "Project1";
    p1.setAttribute('onclick', "swapLinks('Project1')");
    p1.style.marginLeft = '16px';
    const p2 = document.createElement("div");
    p2.classList.add("bp-text");
    p2.textContent = "Project2";
    p2.setAttribute('onclick', "swapLinks('Project2')");
    p2.style.marginLeft = '16px';
    const p3 = document.createElement("div");
    p3.classList.add("bp-text");
    p3.textContent = "Project3";
    p3.setAttribute('onclick', "swapLinks('Project3')");
    p3.style.marginLeft = '16px';

    // Add arrows to each of the bullet points
    act.appendChild(arrow1);
    inactive1.appendChild(arrow2);
    inactive2.appendChild(arrow3);
    inactive3.appendChild(arrow4);
    inactive4.appendChild(arrow5);

    // Assign text to arrows and links based on clicked input
    if (clicked === "Home") {
        act.appendChild(home);
        inactive1.appendChild(about);
        inactive2.appendChild(p1);
        inactive3.appendChild(p2);
        inactive4.appendChild(p3);

        sidebarLinks.appendChild(act);
        sidebarLinks.appendChild(inactive1);
        sidebarLinks.appendChild(inactive2);
        sidebarLinks.appendChild(inactive3);
        sidebarLinks.appendChild(inactive4)
    } else if (clicked ==="About") {
        inactive1.appendChild(home);
        act.appendChild(about);
        inactive2.appendChild(p1);
        inactive3.appendChild(p2);
        inactive4.appendChild(p3);

        sidebarLinks.appendChild(inactive1);
        sidebarLinks.appendChild(act);
        sidebarLinks.appendChild(inactive2);
        sidebarLinks.appendChild(inactive3);
        sidebarLinks.appendChild(inactive4)

    } else if (clicked === "Project1") {
        inactive1.appendChild(home);
        inactive2.appendChild(about);
        act.appendChild(p1);
        inactive3.appendChild(p2);
        inactive4.appendChild(p3);

        sidebarLinks.appendChild(inactive1);
        sidebarLinks.appendChild(inactive2);
        sidebarLinks.appendChild(act);
        sidebarLinks.appendChild(inactive3);
        sidebarLinks.appendChild(inactive4)
    } else if (clicked === "Project2") {
        inactive1.appendChild(home);
        inactive2.appendChild(about);
        inactive3.appendChild(p1);
        act.appendChild(p2);
        inactive4.appendChild(p3);

        sidebarLinks.appendChild(inactive1);
        sidebarLinks.appendChild(inactive2);
        sidebarLinks.appendChild(inactive3);
        sidebarLinks.appendChild(act);
        sidebarLinks.appendChild(inactive4)
    } else if (clicked === "Project3") {
        inactive1.appendChild(home);
        inactive2.appendChild(about);
        inactive3.appendChild(p1);
        inactive4.appendChild(p2);
        act.appendChild(p3);

        sidebarLinks.appendChild(inactive1);
        sidebarLinks.appendChild(inactive2);
        sidebarLinks.appendChild(inactive3);
        sidebarLinks.appendChild(inactive4);
        sidebarLinks.appendChild(act)
    }

    linkContainer.appendChild(sidebarLinks)
    return linkContainer.innerHTML;
}
