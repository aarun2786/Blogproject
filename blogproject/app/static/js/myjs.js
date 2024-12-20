
let bkt = document.getElementById('bkt')
//bkt.style.backgroundColor = "red"
const postCard = ".post-card"
const tagedPostCard = ".taged-post"



function cardDesign(cardClass){
    document.querySelectorAll(cardClass).forEach(post => {
        const mainContent = post.querySelector('.main-content');
        // Create new elements for post image and content
        const postImage = document.createElement('div');
        const postContent = document.createElement('div');
        postImage.className = 'post-card-image';
        postContent.className = 'post-card-content';

        // Move the first image (if exists) into the postImage container
        let index = 4
        const image = mainContent.querySelector('img');
        if (image) {
            index = 5
            postImage.appendChild(image);
            post.insertBefore(postImage,post.children[0]);
        }

        // Move the first text element into the postContent container
        const text = mainContent.querySelectorAll('p');
             for (let i = 0; i<=4; i++){
                let textNode = document.createTextNode(text[i]);
                if (textNode.textContent !== "undefined" ){
                    textNode = document.createTextNode(text[i].innerText+" ")
                    postContent.appendChild(textNode);
                }
                
            }
            
  
        post.insertBefore(postContent,post.children[index]);
        
        // Check if any image not postcard
        if (! image && post.className === "post-card" ){
            post.style.height = "auto"
        }
        // Remove the original main content
        mainContent.remove();
    });
}
cardDesign(postCard)
cardDesign(tagedPostCard)


// post published date formate
function timeformat(date){
    const now = new Date()
    const pubDate = new Date(date)
    
    const seconds = Math.floor((now - pubDate)/1000)
    const year = (seconds / 31536000).toFixed(1)
    const month = Math.floor(seconds / 2592000)
    const week = Math.floor(seconds / 604800)
    const day = Math.floor((seconds / 86400))
    const hour = Math.floor((seconds / 3600))
    const mintus = Math.floor((seconds / 60))
    Math
    //console.log(year,month,day,hour,mintus)
    if(year >= 1){
        return `${year} year ago`
    
    }else if(month >= 1){
        return `${month}mn`
    
    }else if(week >= 1){
        return `${week}w`
    
    }else if(day >= 1){
        return `${day}d`
    
    }else if(hour >= 1){
        return `${hour}hrs`
    
    }else if(mintus >= 1){
    return `${mintus}min`
    
    }else{
        return "just now"
    }   

    


    
}

function updateTime(){
    const pubDate = document.querySelectorAll("#pub_date")
    pubDate.forEach((event ) => {
        const date = event.getAttribute("pub_date")
        event.textContent = timeformat(date)
    })
}
setInterval(updateTime,60000)
updateTime()




// Side Bar function





function hide(element,value){
    // for display block
     const displayStyle = window.getComputedStyle(element).display;
    if (displayStyle == value && window.innerWidth < 1039 ){
        element.style.display = 'none';
    }else{
        element.style.display = value;
    }
    
    
}
let aside = document.getElementsByTagName('aside')[0]
let navbtn = document.getElementById('navbtn')
navbtn.addEventListener('click', () => hide(aside,'block'))

let tags = document.querySelector('.tag')
let asideTagBtn = document.getElementById('aside-tag-btn')
asideTagBtn.addEventListener('click', () => hide(tags,'flex'))

