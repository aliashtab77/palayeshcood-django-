function chLaToPe() {
    const language = document.getElementById("language");
    const form = document.getElementById("changelangugefo");
    language.value = "fa";
    form.submit();
}

function chLaToEn() {
    const language = document.getElementById("language");
    const form = document.getElementById("changelangugefo");
    language.value = "en";
    form.submit();
}

function chLaToAr() {
    const language = document.getElementById("language");
    const form = document.getElementById("changelangugefo");
    language.value = "ar";
    form.submit();
}
function chLaToPeShDe() {
    const language = document.getElementById("language");
    const form = document.getElementById("changelangugefo");
    const penext = document.getElementById("penext");
    const next = document.getElementById("next");
    next.value = penext.value;
    language.value = "fa";
    form.submit();
}

function chLaToEnShDe() {
    const language = document.getElementById("language");
    const form = document.getElementById("changelangugefo");
    const ennext = document.getElementById("ennext");
    const next = document.getElementById("next");
    next.value = ennext.value;
    language.value = "en";
    form.submit();
}

function chLaToArShDe() {
    const language = document.getElementById("language");
    const form = document.getElementById("changelangugefo");
    const arnext = document.getElementById("arnext");
    const next = document.getElementById("next");
    next.value = arnext.value;
    language.value = "ar";
    form.submit();
}