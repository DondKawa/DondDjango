from django.http import HttpResponse

def home(request):
    html_content = """
    <html>
    <head>
        <title>Dond Kawa | Burger King Manager</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f8e9a1; /* Light yellow background */
                margin: 0;
                padding: 0;
                color: #3e1f0d; /* Dark brown text */
            }
            .container {
                max-width: 700px;
                margin: 40px auto;
                padding: 25px;
                background-color: #fff4d1; /* Soft burger yellow */
                border: 2px solid #d72323; /* Burger King red border */
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            header {
                background-color: #d72323; /* Burger King red */
                color: white;
                text-align: center;
                padding: 20px;
                border-radius: 8px 8px 0 0;
                font-size: 24px;
                font-weight: bold;
            }
            section {
                padding: 20px 0;
                border-bottom: 1px solid #e0b000; /* golden yellow */
            }
            section:last-child {
                border-bottom: none;
            }
            h2 {
                color: #b22222; /* Firebrick */
                margin-bottom: 10px;
            }
            ul {
                padding-left: 20px;
            }
            li {
                padding: 5px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>Hello, I'm Dond Kawa!</header>
            <section>
                <h2>About Me</h2>
                <p>I'm the proud manager of Burger King, passionate about leadership, teamwork, and delivering the best burger experience.</p>
            </section>
            <section>
                <h2>What I Enjoy</h2>
                <ul>
                    <li>Motivating my team</li>
                    <li>Enhancing customer service</li>
                    <li>Creating efficient workflows</li>
                </ul>
            </section>
            <section>
                <h2>Current Role</h2>
                <p>I manage day-to-day operations at Burger King, ensuring our customers leave satisfied and our team works in harmony.</p>
            </section>
            <section>
                <h2>Fun Fact</h2>
                <p>I believe that behind every great burger is a greater team. And yes, I do love fries!</p>
            </section>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
