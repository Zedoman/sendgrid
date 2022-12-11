import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *


message = Mail()

message.to = [
    To(
        email="john_doe@example.com",
        name="John Doe",
        p=0
    ),
    To(
        email="julia_doe@example.com",
        name="Julia Doe",
        p=0
    )
]
message.cc = [
    Cc(
        email="jane_doe@example.com",
        name="Jane Doe",
        p=0
    )
]
message.bcc = [
    Bcc(
        email="james_doe@example.com",
        name="Jim Doe",
        p=0
    )
]
message.from_email = From(
    email="sales@example.com",
    name="Example Sales Team",
    p=1
)
message.to = [
    To(
        email="janice_doe@example.com",
        name="Janice Doe",
        p=1
    )
]
message.bcc = [
    Bcc(
        email="jordan_doe@example.com",
        name="Jordan Doe",
        p=1
    )
]

message.from_email = From(
    email="orders@example.com",
    name="Example Order Confirmation"
)

message.reply_to = ReplyTo(
    email="customer_service@example.com",
    name="Example Customer Service Team"
)

message.subject = Subject("Your Example Order Confirmation")

message.content = [
    Content(
        mime_type="text/html",
        content="<p>Hello from Twilio SendGrid!</p><p>Sending with the email service trusted by developers and marketers for <strong>time-savings</strong>, <strong>scalability</strong>, and <strong>delivery expertise</strong>.</p><p>%open-track%</p>"
    )
]

message.attachment = [
    Attachment(
        file_content=FileContent("PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KCiAgICA8aGVhZD4KICAgICAgICA8bWV0YSBjaGFyc2V0PSJVVEYtOCI+CiAgICAgICAgPG1ldGEgaHR0cC1lcXVpdj0iWC1VQS1Db21wYXRpYmxlIiBjb250ZW50PSJJRT1lZGdlIj4KICAgICAgICA8bWV0YSBuYW1lPSJ2aWV3cG9ydCIgY29udGVudD0id2lkdGg9ZGV2aWNlLXdpZHRoLCBpbml0aWFsLXNjYWxlPTEuMCI+CiAgICAgICAgPHRpdGxlPkRvY3VtZW50PC90aXRsZT4KICAgIDwvaGVhZD4KCiAgICA8Ym9keT4KCiAgICA8L2JvZHk+Cgo8L2h0bWw+Cg=="),
        file_name=FileName("index.html"),
        file_type=FileType("text/html"),
        disposition=Disposition("attachment")
    )
]

message.category = [
    Category("cake"),
    Category("pie"),
    Category("baking")
]

message.send_at = SendAt(1617260400)

message.batch_id = BatchId("AsdFgHjklQweRTYuIopzXcVBNm0aSDfGHjklmZcVbNMqWert1znmOP2asDFjkl")

message.asm = Asm(
    group_id=GroupId(12345),
    groups_to_display=GroupsToDisplay([12345])
)

message.ip_pool_name = IpPoolName("transactional email")

message.mail_settings = MailSettings(
    bypass_list_management=BypassListManagement(False),
    footer_settings=FooterSettings(False),
    sandbox_mode=SandBoxMode(False)
)

message.tracking_settings = TrackingSettings(
    click_tracking=ClickTracking(
        enable=True,
        enable_text=False
    ),
    open_tracking=OpenTracking(
        enable=True,
        substitution_tag=OpenTrackingSubstitutionTag("%open-track%")
    ),
    subscription_tracking=SubscriptionTracking(False)
)

sendgrid_client = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
response = sendgrid_client.send(message)

print(response.status_code)
print(response.body)
print(response.headers)
