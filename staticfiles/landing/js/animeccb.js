$(function () {
    let object = document.getElementById("object"), //получаем элмент object
        svgDocument = object.firstElementChild, //получаем svg элемент внутри object
        svgElement = svgDocument.getElementById("wheelleft_inside"), //получаем любой элемент внутри svg
        wheelBBox = svgElement.getBBox(),

        cx = wheelBBox.x + wheelBBox.width / 2,
        cy = wheelBBox.y + +wheelBBox.height / 2,

        t0 = Date.now();

    // Rotate loop
    setInterval(function () {
        var delta = (Date.now() - t0)
        svgElement.setAttribute('transform', 'rotate(' + delta * 0.07 + ', ' + cx + ', ' + cy + ')')
    }, 10);

});
