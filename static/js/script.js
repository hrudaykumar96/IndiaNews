/* login from show whenever page loads */

var loginModal = document.getElementById('loginformModal');
if (loginModal) {
  var modal = new bootstrap.Modal(loginModal);
  modal.show();
}

/* loading effect */

window.addEventListener("load", () => {
  var loader = document.querySelector(".spinner");
  loader.style.display = "none";
});

/* button loader */

function showLoader(button) {
  const loaderButton = document.createElement('button');
  loaderButton.className = 'btn btn-primary';
  loaderButton.type = 'button';
  loaderButton.disabled = true;

  const spinner = document.createElement('span');
  spinner.className = 'spinner-border spinner-border-sm';
  spinner.setAttribute('aria-hidden', 'true');

  const status = document.createElement('span');
  status.setAttribute('role', 'status');
  status.innerText = ' Please Wait....';

  loaderButton.appendChild(spinner);
  loaderButton.appendChild(status);

  button.replaceWith(loaderButton);
  return loaderButton; 
}

function revertToOriginalButton(loaderButton, originalButton) {
  loaderButton.replaceWith(originalButton);
}

/* card loader */

const allSkeleton = document.querySelectorAll('.skeleton')

window.addEventListener('load', function() {
  allSkeleton.forEach(item=> {
    item.classList.remove('skeleton')
  })
})

/* headline scrolling effect start */

document.addEventListener("DOMContentLoaded", function () {
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const cardsContainer = document.querySelector(".cards-container");
  const card = document.querySelector(".card");

  function handleMissingElements() {
    if (prevBtn) prevBtn.style.display = "none";
    if (nextBtn) nextBtn.style.display = "none";
    if (cardsContainer) cardsContainer.style.display = "none";
  }

  if (!prevBtn || !nextBtn || !cardsContainer || !card) {
    handleMissingElements();
    return;
  }

  const cardWidth = card.offsetWidth + 10;

  let isDragging = false;
  let startPos = 0;
  let startScrollPos = 0;
  let scrollPosition = 0;

  function updateButtonVisibility() {
    if (scrollPosition <= 0) {
      prevBtn.style.display = "none";
    } else {
      prevBtn.style.display = "block";
    }

    if (
      scrollPosition >=
      cardsContainer.scrollWidth - cardsContainer.offsetWidth
    ) {
      nextBtn.style.display = "none";
    } else {
      nextBtn.style.display = "block";
    }
  }

  function startDragging(event) {
    isDragging = true;
    startPos = getEventPosition(event);
    startScrollPos = scrollPosition;
    cardsContainer.style.transition = "none";
  }

  function drag(event) {
    if (isDragging) {
      const currentPos = getEventPosition(event);
      const diff = currentPos - startPos;
      scrollPosition = startScrollPos - diff;

      if (scrollPosition < 0) {
        scrollPosition = 0;
      } else if (
        scrollPosition >
        cardsContainer.scrollWidth - cardsContainer.offsetWidth
      ) {
        scrollPosition =
          cardsContainer.scrollWidth - cardsContainer.offsetWidth;
      }

      cardsContainer.style.transform = `translateX(-${scrollPosition}px)`;
    }
  }

  function endDragging() {
    isDragging = false;
    cardsContainer.style.transition = "transform 0.3s ease";
    updateButtonVisibility();
  }

  function getEventPosition(event) {
    return event.type.startsWith("touch")
      ? event.touches[0].clientX
      : event.clientX;
  }

  if (cardsContainer) {
    cardsContainer.addEventListener("touchstart", startDragging);
    cardsContainer.addEventListener("touchmove", drag);
    cardsContainer.addEventListener("touchend", endDragging);
    cardsContainer.addEventListener("mousedown", startDragging);
    cardsContainer.addEventListener("mousemove", drag);
    cardsContainer.addEventListener("mouseup", endDragging);
    cardsContainer.addEventListener("mouseleave", function () {
      if (isDragging) {
        endDragging();
      }
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener("click", function () {
      if (scrollPosition > 0) {
        scrollPosition -= cardWidth;
        if (scrollPosition < 0) {
          scrollPosition = 0;
        }
        cardsContainer.style.transform = `translateX(-${scrollPosition}px)`;
        updateButtonVisibility();
      }
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener("click", function () {
      if (
        scrollPosition <
        cardsContainer.scrollWidth - cardsContainer.offsetWidth
      ) {
        scrollPosition += cardWidth;
        if (
          scrollPosition >
          cardsContainer.scrollWidth - cardsContainer.offsetWidth
        ) {
          scrollPosition =
            cardsContainer.scrollWidth - cardsContainer.offsetWidth;
        }
        cardsContainer.style.transform = `translateX(-${scrollPosition}px)`;
        updateButtonVisibility();
      }
    });
  }

  updateButtonVisibility();
});

/* headline scrolling effect end */

/* toast section */

document.addEventListener("DOMContentLoaded", function () {
  var toastElList = [].slice.call(document.querySelectorAll(".toast"));
  var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl, { autohide: true, delay: 5000 });
  });
  toastList.forEach((toast) => toast.show());
});

/* toast section end */

/* nav active start */

let navLinks = document.querySelectorAll(".nav-link");

navLinks.forEach(function (link) {
  link.addEventListener("click", function (event) {
    navLinks.forEach(function (link) {
      link.classList.remove("active");
    });
    this.classList.add("active");
  });
});

/* nav active end */

/* login form validation */

var formlogin = document.getElementById("form-login");

if (formlogin) {
  formlogin.addEventListener("submit", (e) => {
    e.preventDefault();
    var loginemail = document.getElementById("login-email");
    var loginpassword = document.getElementById("login-password");
    var loginemailerror = document.getElementById("loginemailerror");
    var loginpassworderror = document.getElementById("loginpassworderror");
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (loginemail.value.trim() === "") {
      loginemailerror.innerHTML = "Enter Email";
      loginemail.style.border = "2px solid red";
    } else if (!emailRegex.test(loginemail.value)) {
      loginemailerror.innerHTML = "Enter Valid Email";
      loginemail.style.border = "2px solid red";
    } else {
      loginemailerror.innerHTML = "";
      loginemail.style.border = "2px solid green";
    }
    if (loginpassword.value.trim() === "") {
      loginpassworderror.innerHTML = "Enter Password";
      loginpassword.style.border = "2px solid red";
    } else if (loginpassword.value.length < 8) {
      loginpassworderror.innerHTML = "Password should be atleast 8 characters";
      loginpassword.style.border = "2px solid red";
    } else {
      loginpassworderror.innerHTML = "";
      loginpassword.style.border = "2px solid green";
    }
    if (loginemailerror.innerHTML || loginpassworderror.innerHTML) {
      return;
    }
    var submitButton = document.querySelector("#form-login input[type='submit']");
            if (submitButton) {
                showLoader(submitButton);
            }

            formlogin.submit();
  });
}

/* signup form validation */
var formsignup = document.getElementById("form-signup");

if (formsignup) {
  formsignup.addEventListener("submit", (e) => {
    e.preventDefault();
    var signupname = document.getElementById("signup-name");
    var signupemail = document.getElementById("signup-email");
    var signuppassword = document.getElementById("signup-password").value;
    var signupcnfpassword = document.getElementById("signup-cnfpassword").value;
    var signupnameerror = document.getElementById("signupnameerror");
    var signupemailerror = document.getElementById("signupemailerror");
    var signuppassworderror = document.getElementById("signuppassworderror");
    var signupcnfpassworderror = document.getElementById(
      "signup-cnfpassworderror"
    );
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (signupname.value.trim() === "") {
      signupname.style.border = "2px solid red";
      signupnameerror.innerHTML = "Enter Full Name";
    } else if (signupname.value.length < 3) {
      signupname.style.border = "2px solid red";
      signupnameerror.innerHTML = "Name should be at least 3 characters";
    } else {
      signupname.style.border = "2px solid green";
      signupnameerror.innerHTML = "";
    }

    if (signupemail.value.trim() === "") {
      signupemailerror.innerHTML = "Enter Email";
      signupemail.style.border = "2px solid red";
    } else if (!emailRegex.test(signupemail.value)) {
      signupemailerror.innerHTML = "Enter Valid Email";
      signupemail.style.border = "2px solid red";
    } else {
      signupemailerror.innerHTML = "";
      signupemail.style.border = "2px solid green";
    }

    var personalInfo = [signupname.value, signupemail.value];

    var validationMessage = ValidPassword(signuppassword, personalInfo);

    if (signuppassword.trim() === "") {
      signuppassworderror.innerHTML = "Enter Password";
      document.getElementById("signup-password").style.border = "2px solid red";
    } else if (validationMessage !== "Password is valid.") {
      signuppassworderror.innerHTML = validationMessage;
      document.getElementById("signup-password").style.border = "2px solid red";
    } else {
      signuppassworderror.innerHTML = "";
      document.getElementById("signup-password").style.border =
        "2px solid green";
    }

    if (signupcnfpassword.trim() === "") {
      signupcnfpassworderror.innerHTML = "Enter Confirm Password";
      document.getElementById("signup-cnfpassword").style.border =
        "2px solid red";
    } else if (signupcnfpassword !== signuppassword) {
      signupcnfpassworderror.innerHTML = "Passwords do not match";
      document.getElementById("signup-cnfpassword").style.border =
        "2px solid red";
    } else {
      signupcnfpassworderror.innerHTML = "";
      document.getElementById("signup-cnfpassword").style.border =
        "2px solid green";
    }

    if (
      signupnameerror.innerHTML ||
      signupemailerror.innerHTML ||
      signuppassworderror.innerHTML ||
      signupcnfpassworderror.innerHTML
    ) {
      return;
    }
    var submitButton = document.querySelector("#form-signup button[type='submit']");
    if (submitButton) {
        showLoader(submitButton);
    }

    formsignup.submit();
  });
}

function ValidPassword(password, personalInfo) {
  const lengthRegex =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,20}$/;
  const commonPasswords = [
    "123456",
    "password",
    "123456789",
    "12345678",
    "12345",
    "1234567",
    "1234567890",
    "qwerty",
    "abc123",
    "password1",
  ];

  if (!lengthRegex.test(password)) {
    return "Password must be 8-20 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character.";
  }

  if (commonPasswords.includes(password.toLowerCase())) {
    return "Password is too common. Please choose a different password.";
  }

  for (const info of personalInfo) {
    if (password.toLowerCase().includes(info.toLowerCase())) {
      return "Password is too similar to your personal information.";
    }
  }

  return "Password is valid.";
}

/* reset password form validation */

var resetform = document.getElementById("form-reset");

if (resetform) {
  resetform.addEventListener("submit", function (e) {
    e.preventDefault();
    var resetemail = document.getElementById("reset-email").value;
    var resetpassword = document.getElementById("reset-password").value;
    var resetcnfpassword = document.getElementById("reset-cnfpassword").value;
    var resetemailerror = document.getElementById("resetemailerror");
    var resetpassworderror = document.getElementById("resetpassworderror");
    var resetcnfpassworderror = document.getElementById(
      "resetcnfpassworderror"
    );

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (resetemail.trim() === "") {
      resetemailerror.innerHTML = "Enter Email";
      document.getElementById("reset-email").style.border = "2px solid red";
    } else if (!emailRegex.test(resetemail)) {
      resetemailerror.innerHTML = "Enter Valid Email";
      document.getElementById("reset-email").style.border = "2px solid red";
    } else {
      resetemailerror.innerHTML = "";
      document.getElementById("reset-email").style.border = "2px solid green";
    }

    var personalInfo = [resetemail];

    var validationMessage = isValidPassword(resetpassword, personalInfo);
    if (validationMessage !== "Password is valid.") {
      resetpassworderror.innerHTML = validationMessage;
      document.getElementById("reset-password").style.border = "2px solid red";
    } else {
      resetpassworderror.innerHTML = "";
      document.getElementById("reset-password").style.border =
        "2px solid green";
    }

    if (resetcnfpassword.trim() === "") {
      resetcnfpassworderror.innerHTML = "Enter Confirm Password";
      document.getElementById("reset-cnfpassword").style.border =
        "2px solid red";
    } else if (resetcnfpassword !== resetpassword) {
      resetcnfpassworderror.innerHTML = "Passwords do not match";
      document.getElementById("reset-cnfpassword").style.border =
        "2px solid red";
    } else {
      resetcnfpassworderror.innerHTML = "";
      document.getElementById("reset-cnfpassword").style.border =
        "2px solid green";
    }

    if (
      resetemailerror.innerHTML ||
      resetpassworderror.innerHTML ||
      resetcnfpassworderror.innerHTML
    ) {
      return;
    }
    var submitButton = document.querySelector("#form-reset button[type='submit']");
    if (submitButton) {
        showLoader(submitButton);
    }

    resetform.submit();
  });
}

function isValidPassword(password, personalInfo) {
  const lengthRegex =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,20}$/;
  const commonPasswords = [
    "123456",
    "password",
    "123456789",
    "12345678",
    "12345",
    "1234567",
    "1234567890",
    "qwerty",
    "abc123",
    "password1",
    "email",
    "username",
  ];

  if (!lengthRegex.test(password)) {
    return "Password must be 8-20 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character.";
  }

  if (commonPasswords.includes(password.toLowerCase())) {
    return "Password is too common. Please choose a different password.";
  }

  for (const info of personalInfo) {
    if (password.toLowerCase().includes(info.toLowerCase())) {
      return "Password is too similar to your personal information.";
    }
  }

  return "Password is valid.";
}

/* change password form validation */

var passwordchangeform = document.getElementById("passwordchangeform");

if (passwordchangeform) {
  passwordchangeform.addEventListener("submit", function (e) {
    e.preventDefault();
    var oldpassword = document.getElementById("password-old");
    var changepassword = document.getElementById("password-password").value;
    var changecnfpassword = document.getElementById(
      "password-cnfpassword"
    ).value;
    var oldpassworderror = document.getElementById("oldpassworderror");
    var changepassworderror = document.getElementById("passwordpassworderror");
    var changecnfpassworderror = document.getElementById(
      "passwordcnfpassworderror"
    );

    var personalInfo = [];

    var validationMessage = ValidPassword(changepassword, personalInfo);

    if (oldpassword.value.trim() === "") {
      oldpassword.style.border = "2px solid red";
      oldpassworderror.innerHTML = "Enter Old Password";
    } else if (oldpassword.value.length < 8) {
      oldpassword.style.border = "2px solid red";
      oldpassworderror.innerHTML = "Invalid Password";
    } else {
      oldpassword.style.border = "2px solid green";
      oldpassworderror.innerHTML = "";
    }

    if (validationMessage !== "Password is valid.") {
      changepassworderror.innerHTML = validationMessage;
      document.getElementById("password-password").style.border =
        "2px solid red";
    } else {
      changepassworderror.innerHTML = "";
      document.getElementById("password-password").style.border =
        "2px solid green";
    }

    if (changecnfpassword.trim() === "") {
      changecnfpassworderror.innerHTML = "Enter Confirm Password";
      document.getElementById("password-cnfpassword").style.border =
        "2px solid red";
    } else if (changecnfpassword !== changepassword) {
      changecnfpassworderror.innerHTML = "Passwords do not match";
      document.getElementById("password-cnfpassword").style.border =
        "2px solid red";
    } else {
      changecnfpassworderror.innerHTML = "";
      document.getElementById("password-cnfpassword").style.border =
        "2px solid green";
    }

    if (
      changepassworderror.innerHTML ||
      changecnfpassworderror.innerHTML ||
      oldpassworderror.innerHTML
    ) {
      return;
    }
    var submitButton = document.querySelector("#passwordchangeform button[type='submit']");
    if (submitButton) {
        showLoader(submitButton);
    }

    passwordchangeform.submit();
  });
}

function ValidPassword(password, personalInfo) {
  const lengthRegex =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,20}$/;
  const commonPasswords = [
    "123456",
    "password",
    "123456789",
    "12345678",
    "12345",
    "1234567",
    "1234567890",
    "qwerty",
    "abc123",
    "password1",
  ];

  if (!lengthRegex.test(password)) {
    return "Password must be 8-20 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character.";
  }

  if (commonPasswords.includes(password.toLowerCase())) {
    return "Password is too common. Please choose a different password.";
  }

  for (const info of personalInfo) {
    if (password.toLowerCase().includes(info.toLowerCase())) {
      return "Password is too similar to your personal information.";
    }
  }

  return "Password is valid.";
}

/* add category form validation */
var categoryform = document.getElementById("category-form");

if (categoryform) {
  categoryform.addEventListener("submit", (e) => {
    e.preventDefault();
    var categoryname = document.getElementById("category-name");
    var categoryerror = document.getElementById("category-error");
    if (categoryname.value.trim() === "") {
      categoryname.style.border = "2px solid red";
      categoryerror.innerHTML = "Enter Category";
    } else {
      categoryname.style.border = "2px solid green";
      categoryerror.innerHTML = "";
    }
    if (categoryerror.innerHTML) {
      return;
    }
    var submitButton = document.querySelector("#category-form button[type='submit']");
    if (submitButton) {
        showLoader(submitButton);
    }
    categoryform.submit();
  });
}

/* latest news form validation */
var latest_news_form = document.getElementById("latestnews-form");

if (latest_news_form) {
  latest_news_form.addEventListener("submit", (e) => {
    e.preventDefault();

    var latestnewstitle = document.getElementById("latest_news-title");
    var latestnewsdescriptionEditor = tinymce.get('latest_news-description');
    var latestlatestimageupload = document.getElementById("latest_news-image");
    var latestnewsimageerror = document.getElementById("latest_news-imageerror");
    var latestnewsdescriptionerror = document.getElementById("latest_news-descriptionerror");
    var latestnewserror = document.getElementById("latest_news-titleerror");
    var latestnewscategory = document.getElementById("latestnewscategory");
    var latestnewscategoryerror = document.getElementById("latestnewscategoryerror");
    var latestnewscheck = document.getElementById("latestnewscheck");
    var latestnewscheckerror = document.getElementById("latestnewscheckerror");

    if (latestnewstitle.value.trim() === "") {
      latestnewstitle.style.border = "2px solid red";
      latestnewserror.innerHTML = "Title cannot be empty";
    } else if (latestnewstitle.value.length < 5) {
      latestnewstitle.style.border = "2px solid red";
      latestnewserror.innerHTML = "Title should be at least 5 characters";
    } else {
      latestnewstitle.style.border = "2px solid green";
      latestnewserror.innerHTML = "";
    }

    if (latestnewsdescriptionEditor) {
      var descriptionContent = latestnewsdescriptionEditor.getContent().trim();
      if (descriptionContent === "") {
        document.getElementById("latest_news-description").style.border = "2px solid red";
        latestnewsdescriptionerror.innerHTML = "Description cannot be empty";
      } else if (descriptionContent.length < 5) {
        document.getElementById("latest_news-description").style.border = "2px solid red";
        latestnewsdescriptionerror.innerHTML = "Description should be at least 5 characters";
      } else {
        document.getElementById("latest_news-description").style.border = "2px solid green";
        latestnewsdescriptionerror.innerHTML = "";
      }
    } else {
      document.getElementById("latest_news-description").style.border = "2px solid red";
      latestnewsdescriptionerror.innerHTML = "Editor not initialized";
    }

    if (latestlatestimageupload.files.length === 0) {
      latestnewsimageerror.innerHTML = "Please select an image file";
      latestlatestimageupload.style.border = "2px solid red";
    } else {
      var allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
      if (!allowedExtensions.exec(latestlatestimageupload.value)) {
        latestnewsimageerror.innerHTML = "Invalid file type. Allowed types: .jpg, .jpeg, .png";
        latestlatestimageupload.value = "";
        latestlatestimageupload.style.border = "2px solid red";
        return false;
      } else {
        latestnewsimageerror.innerHTML = "";
        latestlatestimageupload.style.border = "2px solid green";
      }
    }

    if (latestnewscategory.value.trim() === "---------") {
      latestnewscategory.style.border = "2px solid red";
      latestnewscategoryerror.innerHTML = "Select news category";
    } else {
      latestnewscategory.style.border = "2px solid green";
      latestnewscategoryerror.innerHTML = "";
    }

    if (!latestnewscheck.checked) {
      latestnewscheck.style.border = "2px solid red";
      latestnewscheckerror.innerHTML = "Please check the box";
    } else {
      latestnewscheck.style.border = "2px solid green";
      latestnewscheckerror.innerHTML = "";
    }

    if (
      latestnewserror.innerHTML ||
      latestnewsdescriptionerror.innerHTML ||
      latestnewsimageerror.innerHTML ||
      latestnewscategoryerror.innerHTML ||
      latestnewscheckerror.innerHTML
    ) {
      return;
    }
    var submitButton = document.querySelector("#latestnews-form button[type='submit']");
    if (submitButton) {
        showLoader(submitButton);
    }

    latest_news_form.submit();
  });
}

/* trending news form validation */
var trending_news_form = document.getElementById("trendingnews-form");

if (trending_news_form) {
  trending_news_form.addEventListener("submit", (e) => {
    e.preventDefault();

    var trendingnewstitle = document.getElementById("trending_news-title");
    var trendingnewsdescriptionEditor = tinymce.get('trending_news-description');
    var trendingimageupload = document.getElementById("trending_news-image");
    var trendingnewsimageerror = document.getElementById("trending_news-imageerror");
    var trendingnewsdescriptionerror = document.getElementById("trending_news-descriptionerror");
    var trendingnewserror = document.getElementById("trending_news-titleerror");
    var trendingnewscategory = document.getElementById("trendingnewscategory");
    var trendingnewscategoryerror = document.getElementById("trendingnewscategoryerror");
    var trendingnewscheck = document.getElementById("trendingnewschtrending");
    var trendingnewscheckerror = document.getElementById("trendingnewscheckerror");

    if (trendingnewstitle.value.trim() === "") {
      trendingnewstitle.style.border = "2px solid red";
      trendingnewserror.innerHTML = "Title cannot be empty";
    } else if (trendingnewstitle.value.length < 5) {
      trendingnewstitle.style.border = "2px solid red";
      trendingnewserror.innerHTML = "Title should be at least 5 characters";
    } else {
      trendingnewstitle.style.border = "2px solid green";
      trendingnewserror.innerHTML = "";
    }

    if (trendingnewsdescriptionEditor) {
      var descriptionContent = trendingnewsdescriptionEditor.getContent().trim();
      if (descriptionContent === "") {
        document.getElementById("trending_news-description").style.border = "2px solid red";
        trendingnewsdescriptionerror.innerHTML = "Description cannot be empty";
      } else if (descriptionContent.length < 5) {
        document.getElementById("trending_news-description").style.border = "2px solid red";
        trendingnewsdescriptionerror.innerHTML = "Description should be at least 5 characters";
      } else {
        document.getElementById("trending_news-description").style.border = "2px solid green";
        trendingnewsdescriptionerror.innerHTML = "";
      }
    } else {
      document.getElementById("trending_news-description").style.border = "2px solid red";
      trendingnewsdescriptionerror.innerHTML = "Editor not initialized";
    }

    if (trendingimageupload.files.length === 0) {
      trendingnewsimageerror.innerHTML = "Please select an image file";
      trendingimageupload.style.border = "2px solid red";
    } else {
      var allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
      if (!allowedExtensions.exec(trendingimageupload.value)) {
        trendingnewsimageerror.innerHTML = "Invalid file type. Allowed types: .jpg, .jpeg, .png";
        trendingimageupload.value = "";
        trendingimageupload.style.border = "2px solid red";
        return false;
      } else {
        trendingnewsimageerror.innerHTML = "";
        trendingimageupload.style.border = "2px solid green";
      }
    }

    if (trendingnewscategory.value.trim() === "---------") {
      trendingnewscategory.style.border = "2px solid red";
      trendingnewscategoryerror.innerHTML = "Select news category";
    } else {
      trendingnewscategory.style.border = "2px solid green";
      trendingnewscategoryerror.innerHTML = "";
    }

    if (!trendingnewscheck.checked) {
      trendingnewscheck.style.border = "2px solid red";
      trendingnewscheckerror.innerHTML = "Please check the box";
    } else {
      trendingnewscheck.style.border = "2px solid green";
      trendingnewscheckerror.innerHTML = "";
    }

    if (
      trendingnewserror.innerHTML ||
      trendingnewsdescriptionerror.innerHTML ||
      trendingnewsimageerror.innerHTML ||
      trendingnewscategoryerror.innerHTML ||
      trendingnewscheckerror.innerHTML
    ) {
      return;
    }

    var submitButton = document.querySelector("#trendingnews-form button[type='submit']");
    if (submitButton) {
        showLoader(submitButton);
    }

    trending_news_form.submit();
  });
}

/* headlines form validation */

var headlineform = document.getElementById("headline-form");

if (headlineform) {
  headlineform.addEventListener("submit", (e) => {
    e.preventDefault();

    var headlinetitle = document.getElementById("headline-title");
    var headlinedescriptionEditor = tinymce.get('headline-description');
    var headlineimage = document.getElementById("headlineimage");
    var headlinecategory = document.getElementById("headlinecategory");
    var headlinetitleerror = document.getElementById("headlinetitleerror");
    var headlinedescriptionerror = document.getElementById("headlinedescriptionerror");
    var headlinefileerror = document.getElementById("headlinefileerror");
    var headlinecategoryerror = document.getElementById("headlinecategoryerror");
    var headlinecheckmark = document.getElementById("headline-checkmark");
    var headlinecheckmarkerror = document.getElementById("headlinecheckmarkerror");

    if (headlinetitle.value.trim() === "") {
      headlinetitle.style.border = "2px solid red";
      headlinetitleerror.innerHTML = "Title cannot be empty";
    } else if (headlinetitle.value.length < 5) {
      headlinetitle.style.border = "2px solid red";
      headlinetitleerror.innerHTML = "Title should be at least 5 characters";
    } else {
      headlinetitle.style.border = "2px solid green";
      headlinetitleerror.innerHTML = "";
    }

    if (headlinedescriptionEditor) {
      var descriptionContent = headlinedescriptionEditor.getContent().trim();
      if (descriptionContent === "") {
        document.getElementById("headline-description").style.border = "2px solid red";
        headlinedescriptionerror.innerHTML = "Description cannot be empty";
      } else if (descriptionContent.length < 5) {
        document.getElementById("headline-description").style.border = "2px solid red";
        headlinedescriptionerror.innerHTML = "Description should be at least 5 characters";
      } else {
        document.getElementById("headline-description").style.border = "2px solid green";
        headlinedescriptionerror.innerHTML = "";
      }
    } else {
      document.getElementById("headline-description").style.border = "2px solid red";
      headlinedescriptionerror.innerHTML = "Editor not initialized";
    }

    if (headlineimage.files.length === 0) {
      headlinefileerror.innerHTML = "Please select an image file";
      headlineimage.style.border = "2px solid red";
    } else {
      var allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
      if (!allowedExtensions.exec(headlineimage.value)) {
        headlinefileerror.innerHTML = "Invalid file type. Allowed types: .jpg, .jpeg, .png";
        headlineimage.value = "";
        headlineimage.style.border = "2px solid red";
        return false;
      } else {
        headlinefileerror.innerHTML = "";
        headlineimage.style.border = "2px solid green";
      }
    }

    if (headlinecategory.value.trim() === "---------") {
      headlinecategory.style.border = "2px solid red";
      headlinecategoryerror.innerHTML = "Select news category";
    } else {
      headlinecategory.style.border = "2px solid green";
      headlinecategoryerror.innerHTML = "";
    }

    if (!headlinecheckmark.checked) {
      headlinecheckmark.style.border = "2px solid red";
      headlinecheckmarkerror.innerHTML = "Please check the box";
    } else {
      headlinecheckmark.style.border = "2px solid green";
      headlinecheckmarkerror.innerHTML = "";
    }

    if (
      headlinetitleerror.innerHTML ||
      headlinedescriptionerror.innerHTML ||
      headlinefileerror.innerHTML ||
      headlinecategoryerror.innerHTML ||
      headlinecheckmarkerror.innerHTML
    ) {
      return;
    }

    var submitButton = document.querySelector("#headline-form button[type='submit']");
    if (submitButton) {
        showLoader(submitButton);
    }

    headlineform.submit();
  });
}

/* article form validation */
var articleform = document.getElementById("articleform");

if (articleform) {
  articleform.addEventListener("submit", (e) => {
    e.preventDefault();

    var articletitle = document.getElementById("article-title");
    var articledescriptionEditor = tinymce.get('article-description');
    var articleupload = document.getElementById("articleimage");
    var articletitleerror = document.getElementById("articletitleerror");
    var articledescriptionerror = document.getElementById("articledescriptionerror");
    var articlefileerror = document.getElementById("articlefileerror");
    var articlecategory = document.getElementById("articlecategory");
    var articlecategoryerror = document.getElementById("articlecategoryerror");
    var articlecheck = document.getElementById("articlecheckmark");
    var articlecheckerror = document.getElementById("articlecheckmarkerror");

    if (articletitle.value.trim() === "") {
      articletitle.style.border = "2px solid red";
      articletitleerror.innerHTML = "Title cannot be empty";
    } else if (articletitle.value.length < 5) {
      articletitle.style.border = "2px solid red";
      articletitleerror.innerHTML = "Title should be at least 5 characters";
    } else {
      articletitle.style.border = "2px solid green";
      articletitleerror.innerHTML = "";
    }
    if (articledescriptionEditor) {
      var descriptionContent = articledescriptionEditor.getContent().trim();
      if (descriptionContent === "") {
        document.getElementById("article-description").style.border = "2px solid red";
        articledescriptionerror.innerHTML = "Description cannot be empty";
      } else if (descriptionContent.length < 5) {
        document.getElementById("article-description").style.border = "2px solid red";
        articledescriptionerror.innerHTML = "Description should be at least 5 characters";
      } else {
        document.getElementById("article-description").style.border = "2px solid green";
        articledescriptionerror.innerHTML = "";
      }
    } else {
      document.getElementById("article-description").style.border = "2px solid red";
      articledescriptionerror.innerHTML = "Editor not initialized";
    }
    if (articleupload.files.length === 0) {
      articlefileerror.innerHTML = "Please select an image file";
      articleupload.style.border = "2px solid red";
    } else {
      var allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
      if (!allowedExtensions.exec(articleupload.value)) {
        articlefileerror.innerHTML = "Invalid file type. Allowed types: .jpg, .jpeg, .png";
        articleupload.value = "";
        articleupload.style.border = "2px solid red";
        return false;
      } else {
        articlefileerror.innerHTML = "";
        articleupload.style.border = "2px solid green";
      }
    }
    if (articlecategory.value.trim() === "Select News Category") {
      articlecategory.style.border = "2px solid red";
      articlecategoryerror.innerHTML = "Select news category";
    } else {
      articlecategory.style.border = "2px solid green";
      articlecategoryerror.innerHTML = "";
    }
    if (!articlecheck.checked) {
      articlecheck.style.border = "2px solid red";
      articlecheckerror.innerHTML = "Please check the box";
    } else {
      articlecheck.style.border = "2px solid green";
      articlecheckerror.innerHTML = "";
    }
    if (
      articletitleerror.innerHTML ||
      articledescriptionerror.innerHTML ||
      articlefileerror.innerHTML ||
      articlecategoryerror.innerHTML ||
      articlecheckerror.innerHTML
    ) {
      return;
    }

    var submitButton = document.querySelector("#articleform button[type='submit']");
    if (submitButton) {
        showLoader(submitButton);
    }

    articleform.submit();
  });
}

/* admin from validation */

var adminsignupform = document.getElementById("adminsignupform");

if (adminsignupform) {
  adminsignupform.addEventListener("submit", (e) => {
    e.preventDefault();
    var adminname = document.getElementById("adminname");
    var adminnameerror = document.getElementById("adminnameerror");
    var adminemail = document.getElementById("adminemail");
    var adminemailerror = document.getElementById("adminemailerror");
    var adminpassword = document.getElementById("adminpassword");
    var adminpassworderror = document.getElementById("adminpassworderror");
    var admincnfpassword = document.getElementById("admincnfpassword");
    var admincnfpassworderror = document.getElementById(
      "admincnfpassworderror"
    );

    if (adminname.value.trim() === "") {
      adminname.style.border = "2px solid red";
      adminnameerror.innerHTML = "Enter Full Name";
    } else if (adminname.value.length < 3) {
      adminname.style.border = "2px solid red";
      adminnameerror.innerHTML = "Name should be atleadt 3 characters";
    } else {
      adminname.style.border = "2px solid green";
      adminnameerror.innerHTML = "";
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (adminemail.value.trim() === "") {
      adminemail.style.border = "2px solid red";
      adminemailerror.innerHTML = "Enter Email Address";
    } else if (!emailRegex.test(adminemail.value)) {
      adminemail.style.border = "2px solid red";
      adminemailerror.innerHTML = "Enter valid Email";
    } else {
      adminemail.style.border = "2px solid green";
      adminemailerror.innerHTML = "";
    }
    if (adminpassword.value.trim() === "") {
      adminpassword.style.border = "2px solid red";
      adminpassworderror.innerHTML = "Enter Password";
    } else if (adminpassword.value.length < 8) {
      adminpassword.style.border = "2px solid red";
      adminpassworderror.innerHTML = "Password should be atleast 8 characters";
    } else {
      adminpassword.style.border = "2px solid green";
      adminpassworderror.innerHTML = "";
    }
    if (admincnfpassword.value.trim() === "") {
      admincnfpassword.style.border = "2px solid red";
      admincnfpassworderror.innerHTML = "Enter Confirm Password";
    } else if (admincnfpassword.value !== adminpassword.value) {
      admincnfpassword.style.border = "2px solid red";
      admincnfpassworderror.innerHTML = "Password does not match";
    } else {
      admincnfpassword.style.border = "2px solid green";
      admincnfpassworderror.innerHTML = "";
    }
    if (
      adminnameerror.innerHTML ||
      adminemailerror.innerHTML ||
      adminpassworderror.innerHTML ||
      admincnfpassworderror.innerHTML
    ) {
      return;
    }
    var submitButton = document.querySelector("#adminsignupform button[type='submit']");
    if (submitButton) {
        showLoader(submitButton);
    }
    adminsignupform.submit();
  });
}

/* used javascript to delete users */

function delete_user(button) {
  var slug = button.getAttribute("data-slug");
  document.getElementById("delete-user").action = "/delete/" + slug + "/";
}

/* used javascript to delete news */

function delete_news(slug) {
  document.getElementById("delete-user").action = "/deletenews/" + slug + "/";
}

/* used javascript to edit category */

function editcategory(button) {
  var form = document.getElementById("category-form");
  var slug = button.getAttribute("data-slug");
  var name = button.getAttribute("data-name");
  var title = document.getElementById("category-title");
  var category_button = document.getElementById("category-btn");
  var categoryname = document.getElementById("category-name");

  if (slug) {
    title.innerHTML = "Update Category";
    form.action = "/update/category/" + slug + "/";
    categoryname.value = name;
    category_button.innerHTML = "Update Category";
  } else {
    form.reset();
    title.innerHTML = "Add Category";
    form.action = "/add/category/";
    categoryname.value = "";
    category_button.innerHTML = "Add Category";
  }
}
var categoryformModal = document.getElementById("categoryformModal");
categoryformModal.addEventListener("hidden.bs.modal", function () {
  var form = document.getElementById("category-form");
  form.reset();
  var title = document.getElementById("category-title");
  var category_button = document.getElementById("category-btn");
  var form = document.getElementById("category-form");

  title.innerHTML = "Add Category";
  form.action = "/add/category/";
  category_button.innerHTML = "Add Category";
});

/* used javascript to edit users */

function userform(button) {
  var slug = button.getAttribute("user-slug");
  var name = button.getAttribute("user-name");
  var email = button.getAttribute("user-email");
  var role = button.getAttribute("user-role");

  var form = document.getElementById("update_users");
  form.action = "/update/" + slug + "/";

  document.getElementById("updatename").value = name;
  document.getElementById("updateemail").value = email;

  var roleSelect = document.getElementById("updaterole");
  for (var i = 0; i < roleSelect.options.length; i++) {
      if (roleSelect.options[i].value === role) {
          roleSelect.selectedIndex = i;
          break;
      }
  }
}

/* update user validation */

var updateusers = document.getElementById("update_users");

updateusers.addEventListener("submit", (event) => {
  event.preventDefault();
  var updatename = document.getElementById("updatename");
  var updateemail = document.getElementById("updateemail");
  var updatenameerror = document.getElementById("updatenameerror");
  var updateemailerror = document.getElementById("updateemailerror");
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (updatename.value.trim() === "") {
    updatename.style.border = "2px solid red";
    updatenameerror.innerHTML = "Enter Name";
  } else if (updatename.value.length < 3) {
    updatename.style.border = "2px solid red";
    updatenameerror.innerHTML = "Name should be at least 3 characters";
  } else {
    updatename.style.border = "2px solid green";
    updatenameerror.innerHTML = "";
  }

  if (updateemail.value.trim() === "") {
    updateemail.style.border = "2px solid red";
    updateemailerror.innerHTML = "Enter Email Address";
  } else if (!emailRegex.test(updateemail.value)) {
    updateemail.style.border = "2px solid red";
    updateemailerror.innerHTML = "Enter Valid Email";
  } else {
    updateemail.style.border = "2px solid green";
    updateemailerror.innerHTML = "";
  }
  if (
    updatenameerror.innerHTML || updateemailerror.innerHTML 
  ){
    return
  }
  var submitButton = document.querySelector("#update_users button[type='submit']");
  if (submitButton) {
      showLoader(submitButton);
  }
  updateusers.submit();
});

/* news update using javascript */

function updatenews(button) {
  var slug = button.getAttribute("newsdata-slug");
  var baseURL = "/media/";
  document.getElementById("updatenewstitle").value =
    button.getAttribute("newsdata-title");
    
    if (typeof tinymce !== "undefined" && tinymce.get('updatenewsdescription')) {
      tinymce.get('updatenewsdescription').setContent(
        button.getAttribute("newsdata-description")
      );
    }
  document.getElementById("updatenewsimage").src =
    baseURL + button.getAttribute("newsdata-image");
  document.getElementById("updatenewscategory").value =
    button.getAttribute("newsdata-category");
  document.getElementById("update_news").action = "/update/news/" + slug + "/";
}

/* news update validation */

var updatenewsform = document.getElementById("update_news");

updatenewsform.addEventListener("submit", (e) => {
  e.preventDefault();

  var updatenewstitle = document.getElementById("updatenewstitle");
  var updatenewsdescription = tinymce.get('updatenewsdescription');
  var updatenewsnewimage = document.getElementById("updatenewsnewimage");
  var updatenewscategory = document.getElementById("updatenewscategory");
  var updatenewsacknowledge = document.getElementById("updatenewsacknowledge");
  var updatenewstitleerror = document.getElementById("updatenewstitleerror");
  var updatenewsdescriptionerror = document.getElementById("updatenewsdescriptionerror");
  var updatenewsimageerror = document.getElementById("updatenewsimageerror");
  var updatenewscategoryerror = document.getElementById("updatenewscategoryerror");
  var updatenewsacknowledgeerror = document.getElementById("updatenewsacknowledgeerror");

 
  if (updatenewstitle.value.trim() === "") {
    updatenewstitle.style.border = "2px solid red";
    updatenewstitleerror.innerHTML = "Title cannot be empty";
  } else if (updatenewstitle.value.length < 5) {
    updatenewstitle.style.border = "2px solid red";
    updatenewstitleerror.innerHTML = "Title should be at least 5 characters";
  } else {
    updatenewstitle.style.border = "2px solid green";
    updatenewstitleerror.innerHTML = "";
  }


  if (updatenewsdescription) {
    var descriptionContent = updatenewsdescription.getContent().trim();
    if (descriptionContent === "") {
      document.getElementById("updatenewsdescription").style.border = "2px solid red";
      updatenewsdescriptionerror.innerHTML = "Description cannot be empty";
    } else if (descriptionContent.length < 5) {
      document.getElementById("updatenewsdescription").style.border = "2px solid red";
      updatenewsdescriptionerror.innerHTML = "Description should be at least 5 characters";
    } else {
      document.getElementById("updatenewsdescription").style.border = "2px solid green";
      updatenewsdescriptionerror.innerHTML = "";
    }
  } else {
    document.getElementById("updatenewsdescription").style.border = "2px solid red";
    updatenewsdescriptionerror.innerHTML = "Editor not initialized";
  }

  var allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
  if (updatenewsnewimage.files.length > 0) {
    if (!allowedExtensions.exec(updatenewsnewimage.value)) {
      updatenewsnewimage.style.border = "2px solid red";
      updatenewsnewimage.value = "";
      updatenewsimageerror.innerHTML = "Invalid file type. Allowed types: .jpg, .jpeg, .png";
    } else {
      updatenewsnewimage.style.border = "2px solid green";
      updatenewsimageerror.innerHTML = "";
    }
  } else {
    updatenewsnewimage.style.border = "2px solid green";
    updatenewsimageerror.innerHTML = "";
  }

  if (updatenewscategory.value.trim() === "Select News Category") {
    updatenewscategory.style.border = "2px solid red";
    updatenewscategoryerror.innerHTML = "Select a news category";
  } else {
    updatenewscategory.style.border = "2px solid green";
    updatenewscategoryerror.innerHTML = "";
  }

  if (!updatenewsacknowledge.checked) {
    updatenewsacknowledge.style.border = "2px solid red";
    updatenewsacknowledgeerror.innerHTML = "Please check the box";
  } else {
    updatenewsacknowledge.style.border = "2px solid green";
    updatenewsacknowledgeerror.innerHTML = "";
  }

  if (
    updatenewstitleerror.innerHTML ||
    updatenewsdescriptionerror.innerHTML ||
    updatenewsimageerror.innerHTML ||
    updatenewscategoryerror.innerHTML ||
    updatenewsacknowledgeerror.innerHTML
  ) {
    return;
  }
  var submitButton = document.querySelector("#update_news button[type='submit']");
  if (submitButton) {
      showLoader(submitButton);
  }
  updatenewsform.submit();
});

/* post reply */

const reply = (element) => {
  const form = document.querySelector('.reply-form');
  const slug = element.getAttribute('comment-slug');
  const id = element.getAttribute('comment-id');
  
  if (form && slug && id) {
    form.action = `/reply/${id}/${slug}/`;
  }
};

/* delete users */

function delete_category(slug){
  document.getElementById('delete-user').action = "/delete/category/" + slug + "/"
}

/* update profile */

var profileModal = document.getElementById('profileModal');

profileModal.addEventListener('show.bs.modal', function(event) {
  var button = event.relatedTarget;
  
  var name = button.getAttribute('data-profile-name');
  var email = button.getAttribute('data-profile-email');
  var image = button.getAttribute('data-profile-image');
  var description = button.getAttribute('data-profile-description');
  var facebook = button.getAttribute('data-profile-facebook');
  var linkedin = button.getAttribute('data-profile-linkedin');
  var instagram = button.getAttribute('data-profile-instagram');
  var twitter = button.getAttribute('data-profile-twitter');
  var skype = button.getAttribute('data-profile-skype');
  var userId = button.getAttribute('data-profile-user-id');
  
  var form = profileModal.querySelector('#profileform');

  form.action = '/update/profile/' + userId + '/';

  var profileName = form.querySelector('#profileName');
  var profileEmail = form.querySelector('#profileEmail');
  var profileImage = profileModal.querySelector('#profileImage');
  var profileDescription = form.querySelector('#profileDescription');
  var profileFacebook = form.querySelector('#profileFacebook');
  var profileLinkedin = form.querySelector('#profileLinkedin');
  var profileInstagram = form.querySelector('#profileInstagram');
  var profileTwitter = form.querySelector('#profileTwitter');
  var profileSkype = form.querySelector('#profileSkype');

  var baseURL = "/media/";

  if (profileName) profileName.value = name;
  if (profileEmail) profileEmail.value = email;
  if (profileImage) {
    if (image) {
        profileImage.src = baseURL + image;
        profileImage.style.display = 'block';
    } else {
        profileImage.src = ''; 
        profileImage.style.display = 'none'; 
    }
}
  if (profileDescription) profileDescription.value = description;
  if (profileFacebook) profileFacebook.value = facebook;
  if (profileLinkedin) profileLinkedin.value = linkedin;
  if (profileInstagram) profileInstagram.value = instagram;
  if (profileTwitter) profileTwitter.value = twitter;
  if (profileSkype) profileSkype.value = skype;
});

/* update profile validtion */

var profileform = document.getElementById('profileform');

profileform.addEventListener("submit",(e)=>{
  e.preventDefault();
  var profileName = document.getElementById('profileName');
  var profileEmail = document.getElementById('profileEmail');
  var profileNewImage = document.getElementById('profileNewImage');
  var profileFacebook = document.getElementById('profileFacebook');
  var profileLinkedin = document.getElementById('profileLinkedin');
  var profileInstagram = document.getElementById('profileInstagram');
  var profileTwitter = document.getElementById('profileTwitter');
  var profileSkype = document.getElementById('profileSkype');
  var profileDescription = document.getElementById('profileDescription');

  var profilenameerror = document.getElementById('profilename-error');
  var profileemailerror = document.getElementById('profileemail-error');
  var profileimageerror = document.getElementById('profileNewImage-error');
  var profileFacebookError = document.getElementById('profileFacebook-error');
  var profileLinkedinError = document.getElementById('profileLinkedin-error');
  var profileInstagramError = document.getElementById('profileInstagram-error');
  var profileTwitterError = document.getElementById('profileTwitter-error');
  var profileSkypeError = document.getElementById('profileSkype-error');
  var profileDescriptionerror = document.getElementById('profileDescriptionerror');

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  var allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
  const facebookUrlRegex = /^(https?:\/\/)?(www\.)?facebook\.com\/(profile\.php\?id=\d+|[a-zA-Z0-9.]+\/?)$/;
  const linkedinUrlRegex = /^(https?:\/\/)?(www\.)?linkedin\.com\/(in\/[a-zA-Z0-9_-]+|company\/[a-zA-Z0-9_-]+)\/?$/;
  const instagramUrlRegex = /^(https?:\/\/)?(www\.)?instagram\.com\/(p\/[a-zA-Z0-9_-]+|[a-zA-Z0-9._-]+)\/?$/;
  const skypeUrlRegex = /^(skype:[a-zA-Z0-9._-]+(\?call|(\?chat)?)?|https:\/\/(join\.skype\.com\/[a-zA-Z0-9._-]+))$/;
  const twitterUrlRegex = /^(https?:\/\/)?(www\.)?twitter\.com\/(i\/moments\/\d+|[a-zA-Z0-9_]+\/status\/\d+|[a-zA-Z0-9_]+)$/;

  if (profileName.value.trim()===""){
    profileNewImage.style.border="2px solid red";
    profilenameerror.innerHTML="Name Cannot be Empty";
  }
  else if(profileName.value.length<3){
    profileName.style.border="2px solid red";
    profilenameerror.innerHTML = 'Name should be atleast 3 characters'
  }
  else{
    profileName.style.border = '2px solid green';
    profilenameerror.innerHTML = ''
  }
  if(profileEmail.value.trim()===''){
    profileEmail.style.border = '2px solid red';
    profileemailerror.innerHTML = 'Email Cannot be Empty';
  }
  else if(!emailRegex.test(profileEmail.value)){
    profileEmail.style.border = '2px solid red';
    profileemailerror.innerHTML = 'Enter valid Email Address';
  }
  else{
    profileEmail.style.border = '2px solid green';
    profileemailerror.innerHTML = '';
  }
  if (profileNewImage.value.length>0){
    if (!allowedExtensions.test(profileNewImage.value)){
      profileNewImage.style.border = '2px solid red';
      profileNewImage.value =''
      profileimageerror.innerHTML = "Invalid file type. Allowed types: .jpg, .jpeg, .png";
    }
    else{
      profileNewImage.style.border = '2px solid green';
      profileimageerror.innerHTML = '';
    }
  }
  
  else{
    profileNewImage.style.border = '2px solid green';
    profileimageerror.innerHTML = '';
  }

  if(profileFacebook.value.length>0){
    if(!facebookUrlRegex.test(profileFacebook.value.trim())){
      profileFacebook.style.border='2px solid red';
      profileFacebookError.innerHTML = 'Enter Valid url'
    }
    else{
      profileFacebook.style.border='2px solid green';
      profileFacebookError.innerHTML = ''
    }
  }
  else{
    profileFacebook.style.border='2px solid green';
    profileFacebookError.innerHTML = ''
  }
  if(profileLinkedin.value.length>0){
    if(!linkedinUrlRegex.test(profileLinkedin.value.trim())){
      profileLinkedin.style.border='2px solid red';
      profileLinkedinError.innerHTML = 'Enter Valid url'
    }
    else{
      profileLinkedin.style.border='2px solid green';
      profileLinkedinError.innerHTML = ''
    }
  }
  else{
    profileLinkedin.style.border='2px solid green';
    profileLinkedinError.innerHTML = ''
  }
  if(profileInstagram.value.length>0){
    if(!instagramUrlRegex.test(profileInstagram.value.trim())){
      profileInstagram.style.border='2px solid red';
      profileInstagramError.innerHTML = 'Enter Valid url'
    }
    else{
      profileInstagram.style.border='2px solid green';
      profileInstagramError.innerHTML = ''
    }
  }
  else{
    profileInstagram.style.border='2px solid green';
    profileInstagramError.innerHTML = ''
  }
  if(profileTwitter.value.length>0){
    if(!twitterUrlRegex.test(profileTwitter.value.trim())){
      profileTwitter.style.border='2px solid red';
      profileTwitterError.innerHTML = 'Enter Valid url'
    }
    else{
      profileTwitter.style.border='2px solid green';
      profileTwitterError.innerHTML = ''
    }
  }
  else{
    profileTwitter.style.border='2px solid green';
    profileTwitterError.innerHTML = ''
  }
  if(profileSkype.value.length>0){
    if(!skypeUrlRegex.test(profileSkype.value.trim())){
      profileSkype.style.border='2px solid red';
      profileSkypeError.innerHTML = 'Enter Valid url'
    }
    else{
      profileSkype.style.border='2px solid green';
      profileSkypeError.innerHTML = ''
    }
  }
  else{
    profileSkype.style.border='2px solid green';
    profileSkypeError.innerHTML = ''
  }

  if(profileDescription.value.length>0){
    if(profileDescription.value.length>2000){
      profileDescription.style.border='2px solid red';
      profileDescriptionerror.innerHTML = 'Description should not exceeds 3000 characters'
    }
    else{
      profileDescription.style.border='2px solid green';
      profileDescriptionerror.innerHTML = ''
    }
  }
  else{
    profileDescription.style.border='2px solid green';
    profileDescriptionerror.innerHTML = ''
  }

  if(
    profilenameerror.innerHTML ||
    profileemailerror.innerHTML ||
    profileimageerror.innerHTML || profileSkypeError.innerHTML || profileTwitterError.innerHTML || profileInstagramError.innerHTML || profileLinkedinError.innerHTML|| profileFacebookError.innerHTML || profileDescriptionerror.innerHTML
  ){
    return;
  }
  var submitButton = document.querySelector("#update_news button[type='submit']");
  if (submitButton) {
      showLoader(submitButton);
  }
  profileform.submit();
});