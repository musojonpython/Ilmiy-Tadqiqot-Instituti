

function projectHeaderCarousel(){
    alert("Yangi funksiya bajarildi")
    const owl = document.getElementByClass('owl-carousel');
    const homeSlider = document.getElementById('home-slider');
    owl.owlCarousel({
      items: 4, // no. of items
      nav: true, // if you want navigation arrows make it true otherwise false
      dots: true // if you want pagination dots make it true otherwise false
    })
    console.log(owl)
    homeSlider.owlCarousel({
     loop: true,
                margin: 0,
                nav: true,
                dots:false,
                items: 1,
                autoplay: true,
    })

}


//
//$('.owl-carousel').owlCarousel({
//          items: 4, // no. of items
//          nav: true, // if you want navigation arrows make it true otherwise false
//          dots: true // if you want pagination dots make it true otherwise false
//        });
//
//  $('#home-slider').owlCarousel({
//            loop: true,
//            margin: 0,
//            nav: true,
//			dots:false,
//            items: 1,
//            autoplay: true,
//
//        })