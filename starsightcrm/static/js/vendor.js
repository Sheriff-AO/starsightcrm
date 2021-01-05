let updateBtns = document.querySelector('.update-vendor');

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('onclick', function() {
        let siteId = this.dataset.site
        let action = this.dataset.action
        console.log('siteId: ', siteId, 'action: ', action)
    })
}