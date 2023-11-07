var accordion = document.getElementsByClassName('accordion-obj');
var panel = document.getElementsByClassName('accordion-content');
var activeButton = document.getElementsByClassName('active');
var menuUpButton = document.getElementsByClassName('accordion-ico');

for (let index = 0; index < accordion.length; index++) {
    accordion[index].addEventListener("click", function eventAccordionHander(event) {
        if (event.type === "click") {
            if (panel[index].style.display == "none") {
                panel[index].style.display = "block";
                activeButton[index].style.display = "block";
                menuUpButton[index].style.display = "none";
            } else {
                panel[index].style.display = "none";
                menuUpButton[index].style.display = "block";
                activeButton[index].style.display = "none";
            }
        } else {
            return undefined;
        }
    });
}