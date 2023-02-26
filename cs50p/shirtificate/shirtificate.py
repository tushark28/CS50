from fpdf import FPDF

class Shirt(FPDF):

    def get_name(self):
        return input("Enter Name: ").strip()

    def shirtificate_gen(self):
        self.add_page()
        self.set_font("helvetica", "B", size=60)
        self.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self.image("shirtificate.png", w=self.epw)
        self.set_font("Times", size=25)
        self.set_text_color(255,255,255)
        self.text(y=self.eph/2, x=self.epw/3, txt= self.get_name() + " took CS50" )

        self.output("shirtificate.pdf")

def main():
    pdf = Shirt()
    pdf.shirtificate_gen()


if __name__=="__main__":
    main()