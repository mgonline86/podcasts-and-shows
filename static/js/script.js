console.log('hello me')
let adminTools = document.getElementsByClassName("adminVisible");
function adminOn(){
    for (var i=0; i < adminTools.length; i++) {
    adminTools[i].classList.remove('hidden');
    adminTools[i].classList.add('adminBar');
    }
}
function adminOff(){
    for (var i=0; i < adminTools.length; i++) {
        adminTools[i].classList.add('hidden');
        adminTools[i].classList.remove('adminBar');
        }
}