 # **Job Platform 📋**
[**Live Demo**](https://jobs-frontent-react.vercel.app/)

## Overview  

This project is a **Job Platform** designed to connect job seekers and employers seamlessly. It provides an intuitive interface and robust functionality for:  

- **Job Seekers**: Searching and applying for jobs, managing profiles, and tracking applications.  
- **Employers**: Posting job listings, managing applicants, and hiring efficiently.  
- **Admins**: Monitoring platform activities, managing users, and generating reports.  

---

## Features 🚀  

### **Job Seekers**  
1. **Search and Filter Jobs**  
   - Find jobs based on keywords, location, and categories.  

2. **Profile Management**  
   - Create and update profiles with resumes and personal details.  

3. **Application Tracking**  
   - View application statuses and respond to employer messages.  

4. **Job Alerts & Notifications**  
   - Get real-time notifications for new job postings.  

5. **Resume Builder**  
   - Create a resume directly within the platform.  

---

### **Employers**  
1. **Post Job Listings**  
   - Create job postings with detailed requirements.  

2. **Manage Applications**  
   - Review and shortlist candidates efficiently.  

3. **Communicate with Applicants**  
   - Contact candidates for interviews or follow-ups.  

4. **Company Profiles**  
   - Showcase company information and attract top talent.  

---

### **Admins**  
1. **Dashboard**  
   - Monitor site usage, job postings, and user activities.  

2. **User Management**  
   - Approve or revoke access for job seekers and employers.  

3. **Reports & Analytics**  
   - Generate platform analytics and financial statistics.  

4. **Fraud Detection**  
   - Detect and prevent spam or fraudulent job listings.  

---

## Technologies Used 💻  

- **Backend**: Django REST Framework for API development.  
- **Frontend**: React and Tailwind CSS for a dynamic and responsive UI.  
- **Database**: MySQL for reliable and scalable data management.  
- **Authentication**: JWT for secure user authentication.  
- **Styling**: Tailwind CSS for modern design.  
- **Hosting**: Vercel for fast and seamless deployment.  

---

## How It Works 🛠  

### **Job Seekers**  
1. **Sign Up or Login**  
   - Create an account or log in to access job opportunities.  

2. **Search Jobs**  
   - Use filters to find the most relevant opportunities.  

3. **Apply for Jobs**  
   - Submit applications directly from the platform.  

4. **Manage Applications**  
   - Track job application status and receive notifications.  

---

### **Employers**  
1. **Sign Up or Login**  
   - Create an employer account or log in to access the dashboard.  

2. **Post Jobs**  
   - Add job listings with details like job description, requirements, and salary.  

3. **Review Applications**  
   - Manage candidate applications and communicate with potential hires.  

4. **Hire Candidates**  
   - Schedule interviews and finalize hiring decisions.  

---

## Setup and Installation 💾  

### **Frontend**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Emmanuel10701/jobs_python_django.git
   cd job-platform
   ```

2. Install dependencies:  
   ```bash
   npm install
   ```

3. Start the development server:  
   ```bash
   npm run dev
   ```

4. Open the application in your browser:  
   ```
   http://localhost:3000
   ```

---

### **Backend**  
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

2. Run database migrations:  
   ```bash
   python manage.py migrate
   ```

3. Start the Django server:  
   ```bash
   python manage.py runserver
   ```

4. API available at:  
   ```
   http://127.0.0.1:8000/api/
   ```

---

## API Endpoints 📡  

| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | /api/jobs/ | Get all job listings |
| GET | /api/jobs/{id}/ | Get a single job by ID |
| POST | /api/jobs/ | Create a new job listing (Employer) |
| PUT | /api/jobs/{id}/ | Update job details (Employer) |
| DELETE | /api/jobs/{id}/ | Delete a job listing (Admin/Employer) |
| POST | /api/auth/register/ | User registration |
| POST | /api/auth/login/ | User login |

---

## Deployment 🌍  
- **Frontend:** Vercel (Automatic deployment on push to `main` branch).  
- **Backend:** Deployed on AWS EC2 / DigitalOcean (Configurable based on project requirements).  

---

## Contributions 🤝  

Contributions are welcome! If you find a bug or want to add new features, feel free to submit a pull request.  

### **How to Contribute?**  
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature-branch`).  
3. Commit changes (`git commit -m 'Added a new feature'`).  
4. Push to the branch (`git push origin feature-branch`).  
5. Open a pull request.  

---

## License 📜  

This project is open-source and available under the [MIT License](LICENSE).  

---

## Contact 📧  
If you have any questions or feedback, feel free to reach out:  
📩 **Email**: emmanuelmakau90@gmail.com  
🔗 **GitHub**: [Emmanuel10701](https://github.com/Emmanuel10701)  
🚀 **Live Demo**: [Job Platform](https://jobs-frontent-react.vercel.app/)

