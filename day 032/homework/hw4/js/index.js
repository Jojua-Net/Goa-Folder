

const hBtn = document.getElementById("header-btn")
const hNav = document.getElementById("header-nav")

hBtn.addEventListener("click", function() {
    hNav.classList.toggle("open")
    // if (hNav.classList.includes("active")) {

    // }
})

myprojects = () => {
    fetch("projects.json")
    .then(response => response.json())
    .then(data => {
        const myprojects = document.getElementById("myprojects")
        data.forEach(project => {
            const div = document.createElement("div")
            div.classList.add("project-card")

            div.innerHTML = 
            `
            <div class="project-card-img">
                <img src="${project.image}" alt="${project.title}">
            </div>
            
            <div class="project-card-content">
                <div class="br-custom"></div> 
                <span>${project.title}</span>
                <p>${project.content}</p>
            </div>
            `
            myprojects.appendChild(div)
        })
    })

    .catch(error => console.error("შეცდომა:", error));
}


services = () => {
    fetch("services.json")
    .then(response => response.json())
    .then(data => {
        const services = document.getElementById("services")
        data.forEach(service => {
            const div = document.createElement("div")
            div.classList.add("service-card")

            div.innerHTML = 
            `

            <div class="service-card-icon">
                <i class="${service.icon}"></i>
            </div>
            
            <div class="service-card-content">
                <span>${service.title}</span>
                <p>${service.content}</p>
            </div>

            `
            services.appendChild(div)
        })
    })

    .catch(error => console.error("შეცდომა", error))
}




darkLight = () => {
    const body = document.querySelector("body")
    const dLSwitch = document.getElementById("dl-switch")


    if (localStorage.getItem("theme") === "dark") {
        body.classList.add("dark")
    }

    dLSwitch.addEventListener("click", function() {
        body.classList.toggle("dark")

        if (body.classList.contains("dark")) {
            localStorage.setItem("theme", "dark")
        } else {
            localStorage.setItem("theme", "light")
        }
    })
}








services()
myprojects()
darkLight()