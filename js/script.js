//===============================
// Mobile Menu
//===============================

const menuBtn = document.querySelector(".menu-btn");

const navLinks = document.querySelector(".nav-links");

menuBtn.addEventListener("click",()=>{

    navLinks.classList.toggle("show");

});


//===============================
// Sticky Header
//===============================

const header = document.querySelector(".header");

window.addEventListener("scroll",()=>{

    if(window.scrollY>20){

        header.classList.add("scrolled");

    }

    else{

        header.classList.remove("scrolled");

    }

});

const links = document.querySelectorAll(".nav-links a");

links.forEach(link=>{

    link.addEventListener("click",()=>{

        navLinks.classList.remove("show");

    });

});

// for the main-info section
const titles = [

"Technology Educator",

"Computing Teacher",

"IGCSE ICT Teacher",

"Curriculum Designer",

"Teacher Trainer",

"Former Software Developer"

];

let index = 0;

const typingText = document.getElementById("typing-text");

setInterval(()=>{

index++;

if(index >= titles.length){

index = 0;

}

typingText.textContent = titles[index];

},3000);


// Feature Impact Section
// const accordionButtons =
// document.querySelectorAll(".accordion-btn");

// accordionButtons.forEach(button=>{

// button.addEventListener("click",()=>{

// button.classList.toggle("active");

// const content =
// button.nextElementSibling;

// if(content.style.maxHeight){

// content.style.maxHeight=null;

// }else{

// content.style.maxHeight=
// content.scrollHeight+"px";

// }

// });

// });
/*======================================
Render Featured Impact
======================================*/

function renderImpact(){

    const container =
    document.getElementById("impact-container");

    let html="";

    portfolioData.featuredImpact.forEach(project=>{

        html += `

        <article class="impact-item">

            <div class="impact-image">

                <img src="${project.image}" alt="${project.title}">

            </div>

            <div class="impact-content">

                <span class="impact-tag">

                    ${project.category}

                </span>

                <h3>

                    ${project.title}

                </h3>

                <p>

                    ${project.description}

                </p>

                <ul>

                    <li><strong>Role:</strong> ${project.role}</li>

                    <li><strong>Audience:</strong> ${project.audience}</li>

                    <li><strong>Technology:</strong> ${project.technology}</li>

                    <li><strong>Outcome:</strong> ${project.outcome}</li>

                </ul>

            </div>

        </article>

        `;

    });

    container.innerHTML = html;

}

renderImpact();

// Teaching Toolkits
function renderToolkit(){

    const container =
    document.getElementById("toolkit-container");

    let html="";

    portfolioData.toolkit.forEach(tool=>{

    html+=`

    <div class="tool-chip">

    ${tool}

    </div>

    `;

    });

    container.innerHTML=html;

}

renderToolkit();

// Footer Section
/*======================================
Smooth Scroll
======================================*/

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function(e){

        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if(target){

            target.scrollIntoView({

                behavior:"smooth"

            });

        }

    });

});


/*======================================
Scroll Reveal Animation
======================================*/

const revealElements = document.querySelectorAll(".reveal");

function revealOnScroll() {

    const windowHeight = window.innerHeight;

    revealElements.forEach(element => {

        const elementTop =
            element.getBoundingClientRect().top;

        const revealPoint = 100;

        if (elementTop < windowHeight - revealPoint) {

            element.classList.add("active");

        }

    });

}

window.addEventListener("scroll", revealOnScroll);

revealOnScroll();

/*======================================
Animated Statistics Counter
======================================*/

const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {

    const target = Number(counter.dataset.target);
    const suffix = counter.dataset.suffix || "";

    let current = 0;

    const updateCounter = () => {

        const increment = target / 60;

        if (current < target) {

            current += increment;

            counter.textContent =
                Math.ceil(current) + suffix;

            requestAnimationFrame(updateCounter);

        } else {

            counter.textContent =
                target + suffix;

        }
    };

    updateCounter();

});