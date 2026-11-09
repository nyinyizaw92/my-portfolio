from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

def create_water_seller_presentation(filename="Water_Seller_Play_Part4.pptx"):
    prs = Presentation()

    # Define color palette
    NAVY = RGBColor(30, 58, 138)
    DARK_GRAY = RGBColor(51, 51, 51)
    TEAL = RGBColor(13, 148, 136)

    def set_slide_background_and_title(slide, title_text):
        """Helper function to format slide title with consistent styling"""
        title_box = slide.shapes.title
        title_box.text = title_text
        for paragraph in title_box.text_frame.paragraphs:
            paragraph.font.size = Pt(28)
            paragraph.font.bold = True
            paragraph.font.color.rgb = NAVY
            paragraph.font.name = "Pyidaungsu"  # Myanmar Unicode Font

    # -------------------------------------------------------------
    # Slide 1: Title Slide
    # -------------------------------------------------------------
    slide_layout = prs.slide_layouts[0] # Title Slide layout
    slide = prs.slides.add_slide(slide_layout)

    title = slide.shapes.title
    subtitle = slide.placeholders[1]

    title.text = "ရေသည်ပြဇာတ် သင်ကြားရေး လေ့လာဆွေးနွေးချက်"
    subtitle.text = "အပိုင်း (၄) – ရေသည်မိန်းမ၏ စရိုက်၊ ဝတ်စားဆင်ယင်မှုနှင့် ဘဝသဘာဝ\nမြန်မာစာသင်ခန်းစာ လေ့လာသုံးသပ်ချက်"

    for paragraph in title.text_frame.paragraphs:
        paragraph.font.size = Pt(32)
        paragraph.font.bold = True
        paragraph.font.color.rgb = NAVY
        paragraph.font.name = "Pyidaungsu"

    for paragraph in subtitle.text_frame.paragraphs:
        paragraph.font.size = Pt(18)
        paragraph.font.color.rgb = TEAL
        paragraph.font.name = "Pyidaungsu"

    # -------------------------------------------------------------
    # Slide 2: Overview & Paraphrase
    # -------------------------------------------------------------
    slide = prs.slides.add_slide(prs.slide_layouts[1]) # Title & Content layout
    set_slide_background_and_title(slide, "စာပိုဒ်၏ မူရင်းအကောက်နှင့် စကားပြေပြန်ဆိုချက်")

    tf = slide.placeholders[1].text_frame
    tf.word_wrap = True

    p1 = tf.paragraphs[0]
    p1.text = "မူရင်းစာဆို:"
    p1.font.bold = True
    p1.font.size = Pt(20)
    p1.font.color.rgb = NAVY
    p1.font.name = "Pyidaungsu"

    p2 = tf.add_paragraph()
    p2.text = "«တောင်ကြံမြောက်ကြံ၊ ဘရံတောက်တီး၊ ဆင်းရဲကြောင်းကို နိဒါန်းသွယ်လို့...»"
    p2.font.italic = True
    p2.font.size = Pt(18)
    p2.font.color.rgb = DARK_GRAY
    p2.font.name = "Pyidaungsu"

    p3 = tf.add_paragraph()
    p3.text = "\nအဓိပ္ပာယ်ချုပ်:"
    p3.font.bold = True
    p3.font.size = Pt(20)
    p3.font.color.rgb = NAVY
    p3.font.name = "Pyidaungsu"

    bullets_s2 = [
        "ဆင်းရဲဒုက္ခကို ညည်းတွဲနေရုံဖြင့် ဆန်ရမည်မဟုတ်။",
        "လက်တွေ့ကျကျ ရေစွဲစွဲမြဲမြဲ ရောင်းမှသာ ဝမ်းစာပြောင်းဆန် ရရှိမည်။",
        "စုတ်ချာညစ်ပတ်သော ထဘီကို ခါးတင်ထိုးဝတ်၍ မူရာနွဲ့နှောင်းစွာ ရေရောင်းထွက်မည်။",
        "ကာလဒေသ: နံနက်ခင်းအချိန် (နေမမြင့်မီ ရေရောင်းထွက်သည့် ရေသည်မိန်းမ၏ ဘဝပုံရိပ်)"
    ]

    for b in bullets_s2:
        p = tf.add_paragraph()
        p.text = "• " + b
        p.font.size = Pt(16)
        p.font.color.rgb = DARK_GRAY
        p.font.name = "Pyidaungsu"

    # -------------------------------------------------------------
    # Slide 3: Vocabulary Part 1
    # -------------------------------------------------------------
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    set_slide_background_and_title(slide, "ခက်ဆစ်ဖွင့်နှင့် ဝေါဟာရ လေ့လာချက် (အပိုင်း ၁)")

    tf = slide.placeholders[1].text_frame
    tf.word_wrap = True

    vocab_1 = [
        ("တောင်ကြံမြောက်ကြံ", "တောင်ရောက်မြောက်ရောက် ကြံစည်ခြင်း။"),
        ("ဘရံတောက်တီး", "အဓိပ္ပာယ်မရှိဘဲ ရောက်တတ်ရာရာ ('တတ်' ဟု အရေးမှန်ရန် လို)။"),
        ("နိဒါန်းသွယ်လို့", "အကြောင်းစပ်သွယ်လို့ ('စပ်' ဟု အရေးမှန်ရန် လို)။"),
        ("ရေကြပ်ကြပ်", "ဖိဖိစီးစီး၊ စွဲစွဲမြဲမြဲ၊ တွင်တွင်ရောင်းခြင်း။"),
        ("ကုပ်မိမယ်", "ရတုန်း/ကြုံတုန်း အရယူခြင်း (အရပ်သုံး ဗန်းစကား)။")
    ]

    for i, (word, meaning) in enumerate(vocab_1):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {word}: "
        p.font.bold = True
        p.font.size = Pt(18)
        p.font.color.rgb = TEAL
        p.font.name = "Pyidaungsu"

        run = p.add_run()
        run.text = meaning
        run.font.bold = False
        run.font.color.rgb = DARK_GRAY
        run.font.name = "Pyidaungsu"

    # -------------------------------------------------------------
    # Slide 4: Vocabulary Part 2
    # -------------------------------------------------------------
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    set_slide_background_and_title(slide, "ခက်ဆစ်ဖွင့်နှင့် ဝေါဟာရ လေ့လာချက် (အပိုင်း ၂)")

    tf = slide.placeholders[1].text_frame
    tf.word_wrap = True

    vocab_2 = [
        ("စုတ်ပေတောင့်", "စုတ်ချာနိုင်လွန်းလှသော (အညာလေသံ စကားအသုံး)။"),
        ("ဗရဗျစ်", "ရောထွေးစုခဲ ရှုပ်ပွေလျက်။"),
        ("ပဆစ်အိမ်", "ကြွေအံကစားသည့် အကွက်များကဲ့သို့ အစပ်အဖာများ၍ အကွက်ကွက်ဖြစ်နေသော ထဘီ။"),
        ("သုံးလွန်းလိမ် ခါးတင်ထိုး", "ထဘီအထက်နားကို သုံးလိမ်ကျစ်၍ ခါးအထက် (ရင်ရှား) တိုတိုခိုင်ခိုင် ဝတ်ဆင်ခြင်း။")
    ]

    for i, (word, meaning) in enumerate(vocab_2):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"• {word}: "
        p.font.bold = True
        p.font.size = Pt(18)
        p.font.color.rgb = TEAL
        p.font.name = "Pyidaungsu"

        run = p.add_run()
        run.text = meaning
        run.font.bold = False
        run.font.color.rgb = DARK_GRAY
        run.font.name = "Pyidaungsu"

    # -------------------------------------------------------------
    # Slide 5: Table for Literary Devices
    # -------------------------------------------------------------
    slide = prs.slides.add_slide(prs.slide_layouts[5]) # Title Only layout
    set_slide_background_and_title(slide, "အလင်္ကာမြောက် စကားအသုံးများနှင့် စရိုက်ပေါ်လွင်မှု")

    # Add Table
    rows, cols = 5, 3
    left, top, width, height = Inches(0.8), Inches(1.8), Inches(8.4), Inches(4.5)
    table_shape = slide.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table

    table.columns[0].width = Inches(2.5)
    table.columns[1].width = Inches(2.2)
    table.columns[2].width = Inches(3.7)

    headers = ["စကားအသုံး", "အလင်္ကာ / သဘောတရား", "ပေါ်လွင်သည့် အဓိပ္ပာယ်"]
    data = [
        ["ဆန်နီးမယ်မဟုတ်", "ဝင်္ကဝုတ္တိအလင်္ကာ", "ဆန်ရဖို့ အကြောင်းမနီးစပ်ပုံကို သွယ်ဝိုက်ပြောဆိုခြင်း"],
        ["ပြောင်းဆန်ကို ကုပ်မိမယ်", "ဝင်္ကဝုတ္တိအလင်္ကာ", "လက်တွေ့လုပ်ဆောင်မှ ဝမ်းစာရမည်ကို တင်စားခြင်း"],
        ["မှောင်ကျအောင်ညစ်ပါတဲ့", "အတိသယဝုတ္တိအလင်္ကာ", "လုံချည်တစ်ထည်တည်း ကြေးအထပ်ထပ် ညစ်ပတ်ပုံကို လွန်လွန်ကဲကဲ တင်စားခြင်း"],
        ["မူရာတော် နွဲ့နှောင်း", "ဟာသသဘော / စရိုက်", "ရေသည်မိန်းမ၏ ရုပ်သွင်နှင့် ဆန့်ကျင်ဘက်ပြု၍ ဟာသမြောက်အောင် သရုပ်ဖော်ခြင်း"]
    ]

    # Style Header
    for col_idx, text in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = text
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.size = Pt(16)
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.font.name = "Pyidaungsu"
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY

    # Fill Data
    for row_idx, row_data in enumerate(data, start=1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(14)
            p.font.color.rgb = DARK_GRAY
            p.font.name = "Pyidaungsu"

    # -------------------------------------------------------------
    # Slide 6: Teaching Methodology & Takeaways
    # -------------------------------------------------------------
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    set_slide_background_and_title(slide, "သင်ကြားရေးဆိုင်ရာ နည်းလမ်းနှင့် သတိပြုရန်များ")

    tf = slide.placeholders[1].text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "၁။ အရေးအသား မှားယွင်းမှု လျှော့ချရေး:"
    p.font.bold = True
    p.font.size = Pt(18)
    p.font.color.rgb = NAVY
    p.font.name = "Pyidaungsu"

    p_a = tf.add_paragraph()
    p_a.text = "   - ရောက်တတ်ရာရာ ('တက်' ဟု မရေးမိစေရန် သတိပေးရန်)"
    p_a.font.size = Pt(16)
    p_a.font.color.rgb = DARK_GRAY
    p_a.font.name = "Pyidaungsu"

    p_b = tf.add_paragraph()
    p_b.text = "   - အကြောင်းစပ်သွယ် ('ဆက်' ဟု မရေးမိစေရန် သတိပေးရန်)\n"
    p_b.font.size = Pt(16)
    p_b.font.color.rgb = DARK_GRAY
    p_b.font.name = "Pyidaungsu"

    p2 = tf.add_paragraph()
    p2.text = "၂။ စရိုက်သဘာဝ ပေါ်လွင်ပုံ:"
    p2.font.bold = True
    p2.font.size = Pt(18)
    p2.font.color.rgb = NAVY
    p2.font.name = "Pyidaungsu"

    p2_desc = tf.add_paragraph()
    p2_desc.text = "   - စိတ်ကူးယဉ်မနေဘဲ ပြဿနာကို လက်တွေ့ကျကျ ဖြေရှင်းတတ်သည့် ရေသည်မိန်းမ၏ သဘာဝကို ဆွေးနွေးရန်။\n"
    p2_desc.font.size = Pt(16)
    p2_desc.font.color.rgb = DARK_GRAY
    p2_desc.font.name = "Pyidaungsu"

    p3 = tf.add_paragraph()
    p3.text = "၃။ ဇာတ်နှင့် ဆိုင်း ချိတ်ဆက်မှု:"
    p3.font.bold = True
    p3.font.size = Pt(18)
    p3.font.color.rgb = NAVY
    p3.font.name = "Pyidaungsu"

    p3_desc = tf.add_paragraph()
    p3_desc.text = "   - 'အိုးပင့်တော်မူလိုက်စမ်း မောင်ကြီးရှင့်' – ပြဇာတ်စကားပြောမှ ဆိုင်းတီးလုံးသို့ ကူးပြောင်းချိတ်ဆက်သည့် ပြသနည်း။"
    p3_desc.font.size = Pt(16)
    p3_desc.font.color.rgb = DARK_GRAY
    p3_desc.font.name = "Pyidaungsu"

    # Save presentation
    prs.save(filename)
    print(f"PowerPoint file successfully created: {filename}")

if __name__ == "__main__":
    create_water_seller_presentation()