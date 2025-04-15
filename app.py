import streamlit as st

st.set_page_config(page_title="List of Suggested Actions", layout="wide")
st.title("List of Suggested Actions")

# Main function data
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
                "Community psychogeriatric programme (CPGP)", "Eastern community health outreach (ECHO)",
                "Changi Simei Community Care Center"
            ]),
            ("Multidisciplinary team", [
                "Hospital to Home (H2H)", "Our SilverCare Hub (OSH)", "Community intervention team (COMIT)",
                "Community outreach teams (CREST)", "Geriatric day hospital (GDH)", "EAGLECare programme",
                "CGH@Home", "CGH Frail To Fit Clinic"
            ]),
            ("Nurse", [
                "Home nursing", "Centre-based nursing", "Community nursing", "Home medical", "Home therapy"
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
            ("Care coordinator", ["Community case management service (CCMS)", "Care coordinator/case manager", "well being coordinator"]),
            ("Counselling service", ["Hua Mei Counselling and Coaching (HMCC)", "SAGE counselling centre", "O’Joy"]),
            ("Family or friend (close by)", ["Family or friend (close by)"]),
            ("Family or friend (not close by)", ["Family or friend (not close by)"]),
            ("Foreign Domestic Worker (trained as a caregiver)", ["Foreign Domestic Worker (trained as a caregiver)"]),
            ("Helpline services/call centre", ["CareLine", "AIC Hotline", "Touch Help line"]),
            ("High level center based care", [
                "Day care", "Dementia day care", "Day hospice care", "Day rehabilitation",
                "Centre-based nursing", "Night respite", "Geriatric day hospital"
            ])
        ]
    },
    {
        "title": "(3) Care coordination",
        "items": [
            ("Care coordinator (e.g. patient navigators, care manager/coordinators)", ["Community case management service (CCMS)", "Care coordinator/case manager"]),
            ("Family or friend (close by)", ["Family or friend (close by)"]),
            ("Family or friend (not close by)", ["Family or friend (not close by)"]),
            ("Foreign Domestic Worker (trained as a caregiver)", ["Foreign Domestic Worker (trained as a caregiver)"]),
            ("Helpline services/call centre", ["CareLine", "AIC Hotline", "Touch Help line"]),
            ("High level center based care", [
                "Day care", "Dementia day care", "Day hospice care", "Day rehabilitation",
                "Centre-based nursing", "Night respite", "Geriatric day hospital"
            ])
        ]
    }
]

selected_items = []

# --- UI Layout ---
col1, col2 = st.columns(2)

with col1:
    for main in main_functions:
        with st.expander(main["title"], expanded=False):
            for sub_label, sub_items in main["items"]:
                if sub_items:
                    with st.expander(sub_label, expanded=False):
                        selected = st.multiselect(f"Select from {sub_label}", sub_items, key=sub_label + main["title"])
                        for item in selected:
                            selected_items.append((item, main["title"]))

with col2:
    st.subheader("Selected Items Summary")
    if not selected_items:
        st.markdown("*No selections made.*")
    else:
        for item, main_title in selected_items:
            st.markdown(f"- **{item}**  \n↳ _{main_title}_")

