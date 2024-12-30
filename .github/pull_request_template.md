# Your Name
MEGHA SINGH
## Submission checklist


- [x] Your submission follows best practices for [commit messages](https://chris.beams.io/posts/git-commit/) AND for [pull requests](https://github.community/t/best-practices-for-pull-requests/10195)
- [x] `Steps to run the project` AND a `documentation` have been included in a README.md file at root of your project.
- [x] No `binaries/compressed` files have been added
- [x] All pre-existing files in the repository have been removed
- [x] `Screenshots` have been added to the screenshots folder (optional for backend code).
- [x] All italicesed instructions under each submission heading inline, have been removed.
- [x] You understand that a submission here is publicly visible. 
- [x] You have not plagialised, or blatently copied work; and this submission is your original work. (Code of ethics)

## Briefly write about the project that you have submitted from the perspective of the user.
This project is a **Form Builder Application** designed to allow both admins and end users to easily create, manage, fill out, and analyze forms. From the user's perspective, the homepage displays all available forms, which users can click to fill out. End users can anonymously answer various types of questions, such as text, dropdown, and checkboxes, and submit their responses without the need for login. After submission, users are redirected to a "Thank You" page. For admins, the application provides an admin dashboard where they can create and manage forms, view analytics, and gain insights into responses through visualizations like word distributions and option selections. The user interface is clean and centered, ensuring a user-friendly experience with stylish forms, popups, and large fonts for easy interaction.

## Assumptions you have made for this project?
Basic User Roles: There are two primary roles in the system — Admins and End Users. Admins can create and manage forms, while End Users can fill out and submit them.

No Authentication for End Users: End users can submit responses anonymously without the need for login credentials. They can submit responses multiple times without authentication.

Form Structure: A form consists of multiple questions, which can be of three types: Text (open-ended), Dropdown (single-choice from a list), and Checkbox (multiple-choice from a list).

Question Configuration: Each question can have a predefined set of options (for Dropdown and Checkbox types). These options are expected to be provided as a comma-separated string in the database and will be parsed and displayed accordingly.

Response Storage: User responses are stored in JSON format, and each response corresponds to a form. The response is stored in a TextField, and it is processed before being saved to ensure the response data is in a structured format.

Admin Dashboard: Admins can view analytics for each form, including question-level insights such as the distribution of answers for different question types (Text, Dropdown, and Checkbox).

Frontend UI: The user interface for displaying forms, submitting responses, and showing analytics is simple, intuitive, and centered for a clean, user-friendly experience. Some basic styling is applied using CSS for visual appeal.

Data Visualization: Analytics for the form responses are displayed in a basic format such as top word distributions for Text fields and option distributions for Dropdown and Checkbox questions.

## Other information (like testing credentials)
None

## Did you learn anything new while doing this assignment? Please explain.
Learned everything about Django from scratch for this assignment.

## How much time did it take for you complete the project?
4 hours

## If you had more time, what enhancements will you make?
1. better ui
2. More pages to naviagte
3. more functionalities

