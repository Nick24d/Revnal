# Revnal
Revnal is a Django web application designed for developers to manage their journals, share their thoughts publicly, and request code reviews. It features a dual journal system:

- **Private journals** secured by an email and a numeric PIN (format: `pin: ######` or `pin: ####`).
- **Public journals** open for anyone to view.

The app enables seamless management of personal and shared content, with email-based submissions for convenience.

---

## Demo

Try the live app here:  
[working]

### Testing Instructions

- Send an email to the app’s inbound mail address to interact with the system.
- To submit a **code review request**, use the subject line: `review`
- To submit a **journal entry**, use the subject line: `journal`
- For **private journals**, include your PIN in the message body exactly as `pin: 123456` or `pin: 1234` — this PIN is required to view your private messages.
- For **public journals**, do **not** include a PIN.
- Submissions without the correct PIN format for private journals won’t be accessible.

---

## Code Repository

Check out the source code on GitHub:  
[https://github.com/Nick24d/revnal](https://github.com/Nick24d/revnal)

---

## How I Built It

Revnal was built with Django handling the backend and CSS for frontend styling. A key part of the app is its email interaction, powered by **Postmark’s inbound email parsing feature**. Using Postmark simplified receiving and categorizing incoming emails as journal entries or code review requests, allowing users to submit content directly via email.

I started development just two days after discovering similar apps, which inspired me to build a unique solution. ChatGPT helped scaffold parts of the backend logic, especially the differentiation between private and public journals based on PIN validation.
