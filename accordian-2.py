import dash
from dash import html, dcc, Input, Output, State, ALL

app = dash.Dash(__name__)
app.title = "List of Suggested Actions"

# ✅ Updated Data
main_functions = [
    {
        "title": "(1) Support of daily living function",
        "items": [
            ("Assisted living", [
                "Sheltered home", "Destitute home", "Adult disable home"
            ]),
            ("Family or friend (close by)", ["Family or friend (close by)"]),
            ("Family or friend (not close by)", ["Family or friend (not close by)"]),
            ("Foreign Domestic Worker (trained as a caregiver)", ["Foreign Domestic Worker (trained as a caregiver)"]),
            ("High level center based care", [
                "Day care", "Dementia day care", "Day hospice care", "Day rehabilitation",
                "Centre-based nursing", "Night respite", "Geriatric day hospital"
            ]),
            ("IT solution requiring human support", [
                "Red Cross Home Monitoring and Eldercare (HoME+)", "CGH Health Management Unit (tele-education)"
            ]),
            ("Lay Volunteer", [
                "CGH Neighbours", "AIC befriending service", "Health peers", "Montfort Care befriending"
            ]),
            ("Low level center based care", [
                "Community intervention team (COMIT)", "Community outreach teams (CREST)", "Active ageing centre (AAC)",
                "Community rehabilitation centre", "Maintenance day care centre", "Respite care",
                "Senior activity centre (AIC)", "Senior day care", "Community health post",
                "Community psychogeriatric programme (CPGP)", "Eastern community health outreach (ECHO)","Changi Simei Community Care Center"
            ]),
            ("Multidisciplinary team", [
                "Hospital to Home (H2H)", "Our SilverCare Hub (OSH)", "Community intervention team (COMIT)",
                "Community outreach teams (CREST)", "Geriatric day hospital (GDH)", "EAGLECare programme",
                "CGH@Home", "CGH Frail To Fit Clinic"
            ]),
            ("Nurse", [
                "Home nursing", "Centre-based nursing", "Community nursing"," Home medical", "Home therapy"
            ]),
            ("Nursing home", [
                "Nursing home", "EAGLECare Programme (Salvation Army Peacehaven Nursing Home, Moral Home for the Aged Sick, Lions Home for the Elders, NTUC Health Chai Chee Nursing Home, All Saints Home Tampines)"
            ]),
            ("Paid home care aide", [
                "Home Personal Care (HPC)", "Meals-On-Wheels (MOW)", "Medical Escort and Transport (MET)", "Interim caregiver service (ICS)"
            ]),
            ("Support group", [
                "Dementia Singapore", "Stroke Support Station", "SG Enable", "Parkinson Society Singapore support group",
                "TOUCH diabetes support group"
            ])
        ]
    },
    {
        "title": "(2) Social support",
        "items": [
            ("Assisted living", ["Sheltered home", "Destitute home", "Adult disable home"]),
            ("Care coordinator", ["Community case management service (CCMS)", "Care coordinator/case manager","well being coordinator"]),
            ("Counselling service", ["Hua Mei Counselling and Coaching (HMCC)", "SAGE counselling centre", "O’Joy"]),
            ("Family or friend (close by)", ["Family or friend (close by)"]),
            ("Family or friend (not close by)", ["Family or friend (not close by)"]),
            ("Foreign Domestic Worker (trained as a caregiver)", ["Foreign Domestic Worker (trained as a caregiver)"]),
            ("Helpline services/call centre", ["CareLine","AIC Hotline","Touch Help line"]),
            ("High level center based care", ["Day care", "Dementia day care", "Day hospice care", "Day rehabilitation","Centre-based nursing", "Night respite", "Geriatric day hospital"]),        ]
    },
    {
        "title": "(3) Care coordination",
        "items": [
            ("Care coordinator (e.g. patient navigators, care manager/coordinators)", ["Community case management service (CCMS)", "Care coordinator/case manager"]),
            ("Family or friend (close by)", ["Family or friend (close by)"]),
            ("Family or friend (not close by)", ["Family or friend (not close by)"]),
            ("Foreign Domestic Worker (trained as a caregiver)", ["Foreign Domestic Worker (trained as a caregiver)"]),
            ("Helpline services/call centre", ["CareLine","AIC Hotline","Touch Help line"]),
            ("High level center based care", ["Day care", "Dementia day care", "Day hospice care", "Day rehabilitation","Centre-based nursing", "Night respite", "Geriatric day hospital"]),
            



        ]
    }
]

# Components
def sub_accordion(title, subitems, parent_id, main_function_title):
    if subitems:
        return html.Details([
            html.Summary(title, className="sub-summary"),
            dcc.Checklist(
                id={"type": "checklist", "main": main_function_title, "parent": parent_id},
                options=[{"label": item, "value": item} for item in subitems],
                value=[],
                className="checklist"
            )
        ], className="sub-accordion")
    else:
        return html.Details([
            html.Summary(title, className="sub-summary")
        ], className="sub-accordion")

# Layout
app.layout = html.Div([
    html.Div([
        html.H2("List of Suggested Actions", className="header"),
        *[
            html.Details([
                html.Summary(main["title"], className="main-summary"),
                *[sub_accordion(title, subitems, parent_id=title, main_function_title=main["title"])
                  for title, subitems in main["items"]]
            ], className="main-accordion")
            for main in main_functions
        ],
        html.Button("→", id="next-button", n_clicks=0, className="forward-button")
    ], className="left-panel"),

    html.Div([
        html.H2("Selected Items Summary", className="header"),
        html.Div(id="summary-output", className="summary-box")
    ], className="right-panel")
], className="container")

# Callback
@app.callback(
    Output("summary-output", "children"),
    Input("next-button", "n_clicks"),
    State({"type": "checklist", "main": ALL, "parent": ALL}, "value"),
    State({"type": "checklist", "main": ALL, "parent": ALL}, "id")
)
def display_selected(n_clicks, values, ids):
    if not any(values):
        return html.Div("No selections made.", style={"color": "#888", "fontStyle": "italic"})

    output = []
    for val_list, id_dict in zip(values, ids):
        if val_list:
            output.append(
                html.Div([
                    html.Div([
                        html.Div(val, className="selected-pill") for val in val_list
                    ], className="selected-group"),
                    html.Div(f'↳ {id_dict["main"]}', className="selected-function")
                ], className="selected-card")
            )
    return output

# Custom CSS
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background-color: #f9f9f9;
                margin: 0;
                padding: 0;
            }
            .container {
                display: flex;
                padding: 30px;
                gap: 20px;
            }
            .left-panel, .right-panel {
                width: 50%;
                background-color: #fff;
                padding: 20px 30px;
                border-radius: 12px;
                box-shadow: 0 0 12px rgba(0,0,0,0.05);
            }
            .header {
                color: #004e89;
                margin-bottom: 20px;
                font-weight: 600;
            }
            .main-accordion {
                margin-bottom: 20px;
            }
            .main-summary {
                font-weight: bold;
                font-size: 16px;
                cursor: pointer;
            }
            .sub-accordion {
                margin-left: 20px;
                margin-top: 10px;
            }
            .sub-summary {
                font-weight: 500;
                font-size: 14px;
                color: #333;
                cursor: pointer;
            }
            .checklist label {
                display: block;
                margin: 5px 0;
            }
            .forward-button {
                background-color: #004e89;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 18px;
                border-radius: 8px;
                cursor: pointer;
                margin-top: 20px;
                float: right;
            }
            .forward-button:hover {
                background-color: #003e6b;
            }
            .summary-box {
                margin-top: 20px;
            }
            .selected-card {
                margin-bottom: 20px;
                padding: 15px;
                background-color: #f1f8ff;
                border-left: 4px solid #004e89;
                border-radius: 6px;
            }
            .selected-group {
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
            }
            .selected-pill {
                background-color: #cce4f6;
                padding: 5px 10px;
                border-radius: 20px;
                font-size: 13px;
            }
            .selected-function {
                margin-top: 8px;
                font-style: italic;
                color: #555;
                font-size: 13px;
                margin-left: 10px;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == "__main__":
    app.run_server(debug=True)
