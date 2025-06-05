
function getCsrfTokken(formid) {
    return document.getElementById(formid).children[0].value;
}
function newsletterloger(message) {
    const lognews = document.getElementById("newsletterlog");
    lognews.innerHTML = message;
}
function shopcommentloger(message) {
    const logshop = document.getElementById("shopcommentlog");
    logshop.innerHTML = message;
}
function contactuscommentloger(message) {
    const logshop = document.getElementById("contatuslog");
    logshop.innerHTML = message;
}
function contactusfootercommentloger(message) {
    const logshop = document.getElementById("footermessageloger");
    logshop.innerHTML = message;
}

function newsLetter() {
    const csrftoken = getCsrfTokken("newsletter");
    const formurl = document.getElementById("newsletter").action
    const name = document.getElementById("newslettername").value;
    const email = document.getElementById("newsletteremail").value;
    if (email && name && csrftoken){
        const data = {
            name: name,
            email: email
        };
        fetch(formurl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(responseData => {
                newsletterloger(responseData.message);
            })
            .catch(error => {
                newsletterloger(error.message);
            });
    } else {
        return;
    }

}

function shopcomment() {
    const csrftoken = getCsrfTokken("shopcommentform1");
    const formurl = document.getElementById("shopcommentform").action;
    const firstname = document.getElementById("firstnameshop").value;
    const lastname = document.getElementById("lastnameshop").value;
    const phone = document.getElementById("phoneshop").value;
    const email = document.getElementById("emailshop").value;
    const comment = document.getElementById("review-message-shop").value;
    const prikey = document.getElementById("prikey").value;
    if (csrftoken && firstname && comment && prikey){
        const data = {
            name: `${firstname} ${lastname}`,
            email: email,
            phone: phone,
            comment: comment,
            prikey: prikey,

        };
        fetch(formurl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(responseData => {
                shopcommentloger(responseData.message);
            })
            .catch(error => {
                shopcommentloger(error.message);
            });
    } else {
        return;
    }

}

function blogcomment() {
    const csrftoken = getCsrfTokken("blogcommentform1");
    const formurl = document.getElementById("blogcommentform").action
    const firstname = document.getElementById("firstnameblog").value;
    const lastname = document.getElementById("lastnameblog").value;
    const phone = document.getElementById("phoneblog").value;
    const email = document.getElementById("emailblog").value;
    const comment = document.getElementById("review-messageblog").value;
    const prikey = document.getElementById("prikey").value;
    if (csrftoken && firstname && comment && prikey){
        const data = {
            name: `${firstname} ${lastname}`,
            email: email,
            phone: phone,
            comment: comment,
            prikey: prikey,

        };
        fetch(formurl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(responseData => {
                shopcommentloger(responseData.message);
            })
            .catch(error => {
                shopcommentloger(error.message);
            });
    } else {
        return;
    }
}

function contactus() {
    const csrftoken = getCsrfTokken("contactusform");
    const formurl = document.getElementById("contactusform").action;
    const subject = document.getElementById("subjectcontact").value;
    const username = document.getElementById("usernamecontact").value;
    const phone = document.getElementById("phonecontact").value;
    const email = document.getElementById("emailcontact").value;
    const message = document.getElementById("messagecontact").value;
    if (csrftoken && username && email && message){
        const data = {
            name: username,
            email: email,
            phone: phone,
            message: message,
            subject: subject,
        };
        fetch(formurl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(responseData => {
                contactuscommentloger(responseData.message);
            })
            .catch(error => {
                contactuscommentloger(error.message);
            });
    } else {
        return;
    }

}

function contactusfooter() {
    const csrftoken = getCsrfTokken("contactusfooter");
    const formurl = document.getElementById("contactusfooter").action;
    const username = document.getElementById("namefooter").value;
    const email = document.getElementById("emailfooter").value;
    const message = document.getElementById("messagefooter").value;
    if (csrftoken && username && email && message){
        const data = {
            name: username,
            email: email,
            message: message,
        };
        fetch(formurl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(responseData => {
                contactusfootercommentloger(responseData.message);
            })
            .catch(error => {
                contactusfootercommentloger(error.message);
            });
    } else {
        return;
    }

}