!function(e){var t=function(e,t){elementorFrontend.config.breakpoints;var o=e.find(".ct-slick-carousel"),n=o.data(),r={slidesToShow:n.colxl,slidesToScroll:n.slidestoscroll,autoplay:!0===n.autoplay,autoplaySpeed:n.autoplayspeed,infinite:!0===n.infinite,pauseOnHover:!0===n.pauseonhover,speed:n.speed,arrows:!0===n.arrows,dots:!0===n.dots,rtl:!0===n.dir,responsive:[{breakpoint:1200,settings:{slidesToShow:n.collg}},{breakpoint:992,settings:{slidesToShow:n.colmd}},{breakpoint:767,settings:{slidesToShow:n.colsm}},{breakpoint:575,settings:{slidesToShow:n.colxs,slidesToScroll:n.colxs}}]},l=e.find(".ct-slick-nav");l.length>0&&(r.asNavFor=l),void 0!==o.attr("data-centerMode")&&(r.centerMode="true"==o.attr("data-centerMode")),void 0!==o.attr("data-vertical")&&(r.vertical="true"==o.attr("data-vertical")),o.slick(r),t(".ct-nav-carousel").parents(".elementor-element").addClass("hide-nav"),t(".ct-nav-carousel .nav-prev").on("click",(function(){t(this).parents(".elementor-element").find(".slick-prev").trigger("click")})),t(".ct-nav-carousel .nav-next").on("click",(function(){t(this).parents(".elementor-element").find(".slick-next").trigger("click")})),t(".ct-portfolio-carousel4 .ct-portfolio-images .slick-next").on("click",(function(){t(this).parents(".ct-portfolio-carousel4").find(".ct-portfolio-content .slick-next").trigger("click")})),t(".ct-portfolio-carousel4 .ct-portfolio-images .slick-prev").on("click",(function(){t(this).parents(".ct-portfolio-carousel4").find(".ct-portfolio-content .slick-prev").trigger("click")}))};e(".ct-slick-slider").each((function(){var t=e(this).find(".ct-slick-carousel"),o=e(this).find(".ct-slick-nav");e(o).slick({slidesToShow:parseInt(o.attr("data-nav")),slidesToScroll:1,asNavFor:t,dots:!1,arrows:!1,centerMode:!0,infinite:!0,focusOnSelect:!0,autoplay:!1,autoplaySpeed:8e3,speed:800,rtl:!0===o.data("dir"),responsive:[{breakpoint:768,settings:{slidesToShow:1}}]})})),e(window).on("elementor/frontend/init",(function(){elementorFrontend.hooks.addAction("frontend/element_ready/ct_blog_carousel.default",t),elementorFrontend.hooks.addAction("frontend/element_ready/ct_service_carousel.default",t),elementorFrontend.hooks.addAction("frontend/element_ready/ct_portfolio_carousel.default",t),elementorFrontend.hooks.addAction("frontend/element_ready/ct_gallery_carousel.default",t),elementorFrontend.hooks.addAction("frontend/element_ready/ct_testimonial_carousel.default",t),elementorFrontend.hooks.addAction("frontend/element_ready/ct_team_carousel.default",t),elementorFrontend.hooks.addAction("frontend/element_ready/ct_client_carousel.default",t),elementorFrontend.hooks.addAction("frontend/element_ready/ct_feature_carousel.default",t),elementorFrontend.hooks.addAction("frontend/element_ready/ct_award_carousel.default",t),elementorFrontend.hooks.addAction("frontend/element_ready/ct_offer_carousel.default",t)}))}(jQuery);