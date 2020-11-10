document.addEventListener("DOMContentLoaded", () => {

    // get select that has the options available
    const select = document.querySelectorAll("[data-multi-select-plugin]");
    select.forEach(select => {

        init(select);
    });

    // Dismiss on outside click
    document.addEventListener('click', () => {
        // get select that has the options available
        const select = document.querySelectorAll("[data-multi-select-plugin]");
        for (let i = 0; i < select.length; i++) {
            if (event) {
                var isClickInside = select[i].parentElement.parentElement.contains(event.target);

                if (!isClickInside) {
                    const wrapper = select[i].parentElement.parentElement;
                    const dropdown = wrapper.querySelector(".dropdown-icon");
                    const autocomplete_list = wrapper.querySelector(".autocomplete-list");
                    //the click was outside the specifiedElement, do something
                    dropdown.classList.remove("active");
                    autocomplete_list.innerHTML = "";
                    addPlaceholder(wrapper);
                }
            }
        }
    });

});