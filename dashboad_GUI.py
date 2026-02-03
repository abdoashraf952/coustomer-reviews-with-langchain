import streamlit as st
import requests
import pandas as pd
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)

API_URL = "https://tamiko-unidealized-discernibly.ngrok-free.dev/show_reviews"
headers = {"Authorization": "Bearer secret123"}

st.set_page_config(page_title="Review Analysis", layout="wide")

st.title("📊 Customer Reviews Analysis Dashboard")


if st.button("🚀 Start Analysis"):

    with st.spinner("Running analysis... please wait"):
        try:
            res = requests.post(API_URL, headers=headers, verify=False)

            if res.status_code == 200:
                data = res.json()

                problems = data.get("response", [])

                if len(problems) == 0:
                    st.warning("No data returned from API.")
                else:
                    df = pd.DataFrame(problems)

                    st.success("✅ Analysis completed successfully")

                    st.subheader("🔍 Problems Summary")
                    st.dataframe(df, use_container_width=True)

                    st.subheader("📌 Detailed View")
                    for i, item in enumerate(problems, 1):
                        with st.expander(f"Problem {i}: {item['Problem']}"):
                            st.markdown(f"**Number of occurrences:** {item['Number of occurrences']}")
                            st.markdown(f"**Severity level:** {item['Severity level']}")
                            st.markdown("**Suggested Solution:**")
                            st.write(item["Suggested Solution"])

            else:
                st.error(f"❌ Request failed with status code: {res.status_code}")
                st.text(res.text)

        except Exception as e:
            st.error("⚠️ Error while connecting to API")
            st.exception(e)
