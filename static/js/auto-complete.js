// function setupAutocomplete(inputId, resultsId, hiddenId, apiUrl) {
//     const input = document.getElementById(inputId);
//     const results = document.getElementById(resultsId);
//     const hidden = document.getElementById(hiddenId);
//     let debounceTimer;
//     function showSuggestions(query = "") {
//         results.innerHTML = "";
//         fetch(`${apiUrl}?q=${encodeURIComponent(query)}`)
//             .then(response => response.json())
//             .then(data => {
//                 const matches = data || [];
//                 if (matches.length > 0) {
//                     results.classList.remove("d-none");
//                     matches.forEach(match => {
//                         const div = document.createElement("div");
//                         div.textContent = match.name;   // show name
//                         div.classList.add("autocomplete-item");
//                         div.onclick = () => {
//                             input.value = match.name;   // visible input
//                             hidden.value = match.id;    // hidden ID
//                             results.classList.add("d-none");
//                         };
//                         results.appendChild(div);
//                     });
//                 } else {
//                     results.classList.add("d-none");
//                 }
//             })
//             .catch(error => {
//                 console.error("Error fetching:", error);
//                 results.classList.add("d-none");
//             });
//     }
//     function debounce(fn, delay) {
//         return (...args) => {
//             clearTimeout(debounceTimer);
//             debounceTimer = setTimeout(() => fn(...args), delay);
//         };
//     }
//     input.addEventListener("input", debounce(() => {
//         if (input.value.length >= 2) {
//             showSuggestions(input.value);
//         } else {
//             results.classList.add("d-none");
//             hidden.value = ""; // clear ID if input is empty
//         }
//     }, 400));
//     input.addEventListener("focus", () => {
//         if (input.value.length >= 2) {
//             showSuggestions(input.value);
//         }
//     });
//     input.addEventListener("blur", () => {
//         setTimeout(() => results.classList.add("d-none"), 200);
//     });
//     document.addEventListener("click", (e) => {
//         if (!results.contains(e.target) && e.target !== input) {
//             results.classList.add("d-none");
//         }
//     });
// }
// // Initialize for each input
// setupAutocomplete("search-university", "results-university", "search-university-id", "/api/auto-complete/university/");
// setupAutocomplete("search-major", "results-major", "search-major-id", "/api/auto-complete/major/");
// setupAutocomplete("search-lesson", "results-lesson", "search-lesson-id", "/api/auto-complete/lesson/");
// setupAutocomplete("search-teacher", "results-teacher", "search-teacher-id", "/api/auto-complete/teacher/");
