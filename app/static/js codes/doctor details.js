const btns = document.querySelectorAll('.should-select-btn');
const divs = document.querySelectorAll('.should-select-div');
document.addEventListener('DOMContentLoaded', () => {


    btns.forEach(btn => {
        btn.addEventListener('click' , () => {
            // console.log("clicked");
            divs.forEach(div => div.classList.add('hidden'));

            const divId = btn.id.replace('btn' , 'div');
            const relatedDiv = document.getElementById(divId);

            if(relatedDiv){
                relatedDiv.classList.remove('hidden');
            }
        })
    })

})


btns.forEach(btn => {
    btn.addEventListener('click', () => {
        console.log(`Button ${btn.id} clicked`);

        divs.forEach(div => {
            div.classList.add('hidden');
            console.log(`Hiding div ${div.id}`);
        });

        const divId = btn.id.replace('btn', 'div');
        const relatedDiv = document.getElementById(divId);

        if (relatedDiv) {
            console.log(`Showing div ${divId}`);
            relatedDiv.classList.remove('hidden');
        } else {
            console.log(`Div with ID ${divId} not found`);
        }
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const closeButtons = document.querySelectorAll('.close-time');
    const divs = document.querySelectorAll('.should-select-div');

    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            divs.forEach(div => div.classList.add('hidden'));
        });
    });
});