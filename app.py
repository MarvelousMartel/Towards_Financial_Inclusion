import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
#import streamlit.pyplot as st_plt

def load_data():
    # Load the data
    data = pd.read_csv(
        "micro_world.csv",
        encoding='ISO-8859-1'
    )
    return data


def introduction():
    # Write the title and the subheader
    st.title(
        "Empowering Financial Inclusion Through Mobile Financial Services"
    )
    st.subheader(
        """
        What is financial inclusion?
        "Refers to  availability and accessibility of affordable financial services to individuals and businesses, especially those who are excluded or underserved by traditional financial institutions. It aims to provide access to financial services such as savings, credit, insurance, and payments to low-income individuals and businesses, enabling them to manage their financial lives effectively and participate fully in the economy."
        """
    )
    st.markdown(
        "Source: Financial Inclusion Overview, World Bank (2021)"
    )
    st.subheader(
        """
        Mobile Financial Services
        According to the International Telecommunication Union (ITU), these are "services such as mobile-enabled payment systems and mobile banking with security and convenience for transfers, payments and savings through the concept of a ‘mobile wallet’ account ".
        """
    )
    st.subheader(
        """
        The Question:
        How do we empower financial inclusion through mobile financial services?
        """
    )
    st.subheader(
        """
        The Data We Are Using:
        The 2021 Global Financial Inclusion (Global Findex)  Survey consists of a total of 127,854 respondents; 1,000 of them are Filipinos.
        """
    )
    st.subheader(
        """
        Mobile Ownership in the Philippines:
        97 out of 100 Filipinos are mobile owners
        """
    )


def Mobile_Onwership_And_Utility():
    st.title("Mobile Ownership & Utility: Philippines VS The World")
    st.subheader(
        """
        Mobile Ownership:
        The Philippines has a higher percentage of mobile phone owners than the rest of the world.
        With this said, we may perhaps speculate that more Filipinos should be using their phones to access financial services.
        However, this is not the case.
        """
    )

    # Insert Phil VS World: Mobile Ownership chart here
    # Load the data
    data = pd.read_csv('micro_world.csv', encoding='ISO-8859-1')
    # Filter the data
    philippine_data = data[
        data['economy'] == 'Philippines'
        ]
    # Filter data for the REST OF THE WORLD
    ROTW_data = data[~data.isin(philippine_data)]
    len_ROTW = len(data) - len(philippine_data)
    # Filter data: variable = mobileowner
    has_mobile_ROTW = ROTW_data[ROTW_data["mobileowner"] == 1]
    has_mobile_ph = philippine_data[philippine_data["mobileowner"] == 1]
    # Compute Percentage
    percent_has_mobile_ph = len(has_mobile_ph) * 100.0 / len(philippine_data)
    percent_has_mobile_ROTW = len(has_mobile_ROTW) * 100.0 / len_ROTW
    # Plot bar graph

    # Set figure size
    plt.figure(figsize=(6, 5), dpi=150)

    phil_vs_world = pd.DataFrame()

    phil_vs_world["Philippines"] = [percent_has_mobile_ph]
    phil_vs_world["World"] = [percent_has_mobile_ROTW]

    phil_vs_world = phil_vs_world.rename(
        index={0: "% of Mobile Ownership", 1: "Philippines", 2: "World"}).transpose().squeeze()

    # create a bar graph from the dataframe
    ax = phil_vs_world.plot(kind='bar')

    # iterate over the bars
    for i in ax.containers:
        # iterate over the bar segments (which correspond to each bar section)
        for j in i:
            # get the height of the bar segment
            height = j.get_height()
            # add the text label to the bar segment
            ax.annotate(f'{height:.2f}', xy=(j.get_x() + j.get_width() / 2, height),
                        xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')

    phil_vs_world.plot.bar(title="Phil vs World: Mobile Ownership", rot=0, color=['#fb8500', '#219ebc'], width=.8,
                           ylim=(80, 100))
    plt.ylabel('% of Mobile Owners')
    st.pyplot(plt)

    st.subheader(
        """
        Mobile Phone Utility:
        The Philippines has  a lower percentage of mobile phone utility than the rest of the world in terms of accessing account and checking account balance.
        """
    )
    # Insert Mobile Phone Utility: Phil vs World chart here
    # Filter data: variables = AccessAaccount(fin5); CheckAccount(fin6)
    mobileAccess_account_ph = philippine_data[philippine_data["fin5"] == 1]
    mobileAccess_account_ROTW = ROTW_data[ROTW_data["fin5"] == 1]

    mobileCheck_bal_ph = philippine_data[philippine_data["fin6"] == 1]
    mobileCheck_bal_ROTW = ROTW_data[ROTW_data["fin6"] == 1]

    # Compute Percentage
    percent_mobileAccess_account_ph = len(mobileAccess_account_ph) * 100.0 / len(philippine_data)
    percent_mobileAccess_account_ROTW = len(mobileAccess_account_ROTW) * 100.0 / len_ROTW

    percent_mobileCheck_bal_account_ph = len(mobileCheck_bal_ph) * 100.0 / len(philippine_data)
    percent_mobileCheck_bal_ROTW = len(mobileCheck_bal_ROTW) * 100.0 / len_ROTW
    # Create horizontal bar graph
    MobileUtility_philVsWorld = pd.DataFrame({
        'Mobile Utility': ["To access \n account", "To check \n account \n balance"],
        'Philippines': [percent_mobileAccess_account_ph, percent_mobileCheck_bal_account_ph],
        'World': [percent_mobileAccess_account_ROTW, percent_mobileCheck_bal_ROTW]
    })
    # Set the Mobile Utility column as the index
    MobileUtility_philVsWorld = MobileUtility_philVsWorld.set_index('Mobile Utility')

    # Set bar plot
    # Set figure size
    plt.figure(figsize=(6, 3), dpi=20000)

    # Create a horizontal bar graph
    ax = MobileUtility_philVsWorld.plot(kind='barh', color=['#fb8500', '#219ebc'], rot=0, width=.6)
    for i in ax.containers:
        # iterate over the bar segments (which correspond to each bar section)
        for j in i:
            # get the width of the bar segment
            width = j.get_width()
            # add the text label to the bar segment
            ax.annotate(f'{width:.2f}', xy=(width, j.get_y() + j.get_height() / 2),
                        xytext=(3, 0), textcoords='offset points', ha='left', va='center')

    # Create a horizontal bar graph
    plt.xticks(range(0, 51, 10))

    # Add labels and title
    plt.xlabel('% of Mobile Owners')
    plt.ylabel('')
    plt.title('Mobile Phone Utility: Phil vs World')

    # Show the plot
    st.pyplot(plt)

def Is_there_a_disparity():
    # reading the data
    data = pd.read_csv('micro_world.csv', encoding='ISO-8859-1')
    philippine_data = data[data["economy"] == "Philippines"]
    st.title("Is it possible that educational attainment and income level may affect mobile phone usage for financial services?")

    st.subheader(
        """
        We found that there is not much disparity among the percentage of mobile owners in terms of educational attainment.
        Most of those sampled in the survey (576 out of 1,000), who completed secondary school had a mobile device. 97% of them had a mobile device.
        """
        )
    # Insert chart on % population with mobile per educ attainment
    # create a column for has mobile
    philippine_data['has_mobile'] = philippine_data['mobileowner'].apply(lambda x: 1 if x == 1 else 0)
    # use .agg() to sum has_mobile and count wpid_random
    educ_mobile_data = philippine_data.groupby(['educ']).agg(
        total_mobile_owners=('has_mobile', 'sum'),
        total_population=('wpid_random', 'count')
    ).reset_index()

    # assign data to variables
    totmob = educ_mobile_data["total_mobile_owners"]
    totpop = educ_mobile_data["total_population"]

    # compute percent mobile users per population
    educ_mobile_data["%_has_mobile"] = (totmob / totpop) * 100
    # create a horizontal bar chart with Pandas
    ax = educ_mobile_data.plot(kind='barh', x='educ', y='%_has_mobile', color='orange', width=0.8)

    # set the figure DPI
    ax.get_figure().set_dpi(300)

    # Set title
    plt.title('% Population with Mobile per Educ Attainment')

    # Set labels
    plt.xlabel('% with Mobile')
    plt.ylabel('Educational Attainment')
    plt.xlim(80, 100)

    # Show figure
    st.pyplot(plt)

    st.subheader(
        """
        We also found only a slight disparity among the percentage of mobile owners in terms of income group.
        There was only a 3 to 4% difference from the middle 20% to the richest 20% and poorest 20%
        """
    )
    # Insert chart on % mobile phone ownership per income group
    # create a column for has mobile
    philippine_data['has_mobile'] = philippine_data['mobileowner'].apply(lambda x: 1 if x == 1 else 0)

    # use .agg() to sum has_mobile and count wpid_random
    income_mobile_data = philippine_data.groupby(['inc_q']).agg(
        total_mobile_owners=('has_mobile', 'sum'),
        total_population=('wpid_random', 'count')
    ).reset_index()

    # assign data to to variables
    totmob = income_mobile_data["total_mobile_owners"]
    totpop = income_mobile_data["total_population"]

    # compute percent mobile users per population
    income_mobile_data["%_has_mobile"] = (totmob / totpop) * 100

    # Create a dictionary for mapping
    income_group_mapping = {
        1: 'Poorest 20%',
        2: 'Second 20%',
        3: 'Middle 20%',
        4: 'Fourth 20%',
        5: 'Richest 20%'
    }
    income_mobile_data = income_mobile_data.replace({'inc_q': income_group_mapping})
    plt.figure(figsize=(6, 3), dpi=200)

    # Run bar plot
    plt.bar(
        income_mobile_data["inc_q"],
        income_mobile_data["%_has_mobile"],
        color="orange", width=.8
    )

    # Set title
    plt.title("% Mobile Phone Ownership per Income Group")

    ax = plt.plot()

    # Set labels
    plt.xlabel('Income Group')
    plt.ylabel('% with Mobile')

    # Rotate x labels
    plt.xticks(rotation=0)
    plt.ylim(80, 100)
    plt.tick_params(axis='x', which='major', labelsize=8.2)

    # Show figure
    st.pyplot(plt)

    st.subheader(
        """
        From this data, we can deduce that device ownership is more or less equally distributed in terms of  educational attainment and income.
        So what makes mobile utility in the Philippines lower, despite having a higher rate of mobile ownership?
        """
    )

def Mobile_VS_Traditional():
    # Load the data
    data = pd.read_csv('micro_world.csv', encoding='ISO-8859-1')
    # Filter the data
    philippine_data = data[
        data['economy'] == 'Philippines'
        ]

    st.title("""
    Mobile Money Usage Compared with Traditional Means
    """
    )
    st.subheader(
        """
        Let us take a look at mobile money usage compared with traditional means.
        In today's digital age, more and more people are turning to mobile phones as a means of managing their finances. In the Philippines, data shows that a significant number of people have used their mobile phones for in-store purchases and to access mobile banking services. However, despite the growing popularity of mobile banking, many people still prefer traditional financial institutions.
        """
    )

    st.markdown(
        """
        According to the data, 17.7% of Filipinos have used their mobile phones for in-store purchases, while 14.5% and 7.3% have used debit and credit cards, respectively. This suggests that trust is not a major issue when it comes to using mobile phones for payments, and that mobile phones are more accessible than traditional banking cards.
        """
    )
    # insert table on cashless in-store purchases
    ROTW_data = data[~data.isin(philippine_data)]
    has_mobile_ROTW = ROTW_data[ROTW_data["mobileowner"] == 1]
    len_ROTW = len(data) - len(philippine_data)

    fin14_1data = philippine_data[["fin14_1"]]
    fin4adata = philippine_data[["fin4a"]]
    fin8adata = philippine_data[["fin8a"]]
    mobilePay_purchase_ph = philippine_data[philippine_data["fin14_1"] == 1]
    mobilePay_purchase_ROTW = ROTW_data[ROTW_data["fin14_1"] == 1]

    percent_mobilePay_purchase_ph = len(mobilePay_purchase_ph) * 100.0 / len(philippine_data)
    percent_mobilePay_purchase_ROTW = len(mobilePay_purchase_ROTW) * 100.0 / len_ROTW

    paid_using_debit_ph = philippine_data[philippine_data["fin4a"] == 1]
    paid_Not_using_debit_ph = philippine_data[philippine_data["fin4a"] == 2]

    # Compute the Percentage
    percent_paid_using_debit_ph = len(paid_using_debit_ph) * 100.0 / len(philippine_data)
    percent_paid_Not_using_debit_ph = len(paid_Not_using_debit_ph) * 100.0 / len(philippine_data)

    paid_using_credit_ph = philippine_data[philippine_data["fin8a"] == 1]
    paid_Not_using_credit_ph = philippine_data[philippine_data["fin8a"] == 2]

    # Compute the Percentage
    percent_paid_using_credit_ph = len(paid_using_credit_ph) * 100.0 / len(philippine_data)
    percent_paid_Not_using_credit_ph = len(paid_Not_using_credit_ph) * 100.0 / len(philippine_data)

    # Plot bar graph

    # Set figure size
    plt.figure(figsize=(6, 5), dpi=150)

    phil_payment_comparison2 = pd.DataFrame()

    phil_payment_comparison2["Mobile Phone"] = [percent_mobilePay_purchase_ph]
    phil_payment_comparison2["Debit Card"] = [percent_paid_using_debit_ph]
    phil_payment_comparison2["Credit Card"] = [percent_paid_using_credit_ph]

    phil_payment_comparison2 = phil_payment_comparison2.rename(
        index={0: "% of Filipinos", 1: "Mobile Phone", 2: "Debit Card", 3: "Credit Card"}).transpose().squeeze()

    # create a bar graph from the dataframe
    ax = phil_payment_comparison2.plot(kind='bar')

    # iterate over the bars
    for i in ax.containers:
        # iterate over the bar segments (which correspond to each bar section)
        for j in i:
            # get the height of the bar segment
            height = j.get_height()
            # add the text label to the bar segment
            ax.annotate(f'{height:.2f}', xy=(j.get_x() + j.get_width() / 2, height),
                        xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')

    phil_payment_comparison2.plot.bar(title="Cashless In-store Purchases in the Philippines", rot=0,
                                      color=['#fb8500', '#219ebc', '#023047'], width=.8, ylim=(0, 25))

    # Add labels and title
    plt.xlabel('Payment Method')
    plt.ylabel('% of Filipinos')
    st.pyplot(plt)

    st.markdown(
        """
        Despite the growing popularity of mobile banking, traditional financial institutions still hold significant appeal among the Filipino population. In fact, 98% of those who store money with traditional accounts have mobile devices, indicating that most Filipinos still prefer to use traditional accounts over mobile banking.
        The data also shows that 16% of the sample used a mobile account to store money, indicating a gap in knowledge or access to mobile banking services.
        """
    )
    st.metric(label="Percentage of those with traditional account that have mobile devices.", value=98)
    st.metric(label="Percentage of thsoe who have used mobile account to store money.", value=16)


    st.subheader(
        """
        Furthermore, the data reveals that Filipinos prefer the traditional way of saving over mobile banking services.
        For instance, 28.2% saved their money in financial institutions, as opposed to 12.8% who used mobile banking services to save money. This could be due to a lack of trust, difficulty in accessing the services, lack of education, or cultural bias towards traditional banking institutions.
        """
    )
    # insert table on preference to save money
    # Comparing percentages between fin17a and fin17a1
    savedin_financial_inst = len(philippine_data[philippine_data["fin17a"] == 1]) * 100.0 / len(philippine_data)
    savedin_mobile = len(philippine_data[philippine_data["fin17a1"] == 1]) * 100.0 / len(philippine_data)

    # Plot bar graph

    # Set figure size
    plt.figure(figsize=(6, 5), dpi=150)

    fininstitution_vs_mobile = pd.DataFrame()

    fininstitution_vs_mobile["At a Financial Institution"] = [savedin_financial_inst]
    fininstitution_vs_mobile["Using Mobile Money Account"] = [savedin_mobile]

    fininstitution_vs_mobile = fininstitution_vs_mobile.rename(
        index={0: "% of Filipinos", 1: "At a Financial Institution",
               2: "Using Mobile Money Account"}).transpose().squeeze()

    # create a bar graph from the dataframe
    ax = fininstitution_vs_mobile.plot(kind='bar')

    # iterate over the bars
    for i in ax.containers:
        # iterate over the bar segments (which correspond to each bar section)
        for j in i:
            # get the height of the bar segment
            height = j.get_height()
            # add the text label to the bar segment
            ax.annotate(f'{height:.2f}', xy=(j.get_x() + j.get_width() / 2, height),
                        xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')

    fininstitution_vs_mobile.plot.bar(title="Preference to Save Money", rot=0, color=['#fb8500', '#219ebc'], width=.8,
                                      ylim=(0, 35))

    plt.ylabel('% of Filipinos')
    st.pyplot(plt)

    st.subheader(
        """
        In terms of borrowing money, the data shows that 93% of Filipino borrowers prefer other means than mobile banking, with 3 out of 4 of those borrowers preferring to borrow from family or friends.
        These are usually middle to rich income, educated, and employed people. This could be an opportunity for employers to take advantage of by collaborating with mobile banking providers to offer exclusive loan products, discounts, or incentives.
        """
    )

def Insights_and_reco():
    st.title(
        """
        Let's go back to The Question: How do we empower financial inclusion through mobile financial services?
        """
    )
    st.subheader(
        """
        For Paying: Continue to leverage the acceptance of mobile payment by consumers and merchants
        Focus on MSMEs for merchants:\n
            Credit Lines\n
            Lower Onboarding Fees\n
            Business Analytics
        """
    )
    st.subheader(
        """
        For Saving: Incentivize savings:\n
            Nano-loans for regular savers\n
            Automated micro savings by rounding off
        """
    )
    st.subheader(
        """
        For Borrowing: Engage partnerships between employers and mobile banking providers:\n
            Salary advances\n
            Mobile-based group lending (i.e., Health Related Emergencies)
        """
    )

def the_team():
    # Write the title
    st.title(
        "The Team"
    )
    st.subheader("Quenie Alaton")
    st.subheader("Harold Lopez")
    st.subheader("Martel Espiritu")

list_of_pages = [

    "Introduction",
    "Mobile Ownership & Utility",
    "Is There a Disparity Among Groups?",
    "Mobile Money Usage VS Traditional",
    "Insights and Recommendations",
    "The Team"
]

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()

elif selection == "Mobile Ownership & Utility":
    Mobile_Onwership_And_Utility()

elif selection == "Is There a Disparity Among Groups?":
    Is_there_a_disparity()

elif selection == "Mobile Money Usage VS Traditional":
    Mobile_VS_Traditional()

elif selection == "Insights and Recommendations":
    Insights_and_reco()

elif selection == "The Team":
    the_team()
