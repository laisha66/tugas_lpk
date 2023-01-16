import streamlit as st


video_file = open('silucu.mp4','rb')
video_bytes = video_file.read()
        
st.video(video_bytes) 
    
st.title('Ini adalah aplikasi penentuan pH suatu larutan')       

tombol=st.button('OLEH KELOMPOK 3')
if tombol:
    st.write('Laisha Awiana Maharani')
    st.write('Muhammad Ridwan')
    st.write('Putra Harapan Mahmuddin')
    st.write('Salwaa Nuhaa Nazhira')
    st.write('Siti Nur Aziizah Rustam')


st.image("https://s4.aconvert.com/convert/p3r68-cdx67/aslr1-knu3u.jpg",width=100,)
NamaLarutan=st.text_input('Nama Larutan yang akan dicari pH')

st.write('Silahkan pilih jenis larutan dengan format "asam kuat" "asam lemah" "basa kuat" ataupun "basa lemah" jika format yang dimasukan salah maka web tidak akan bekerja silahkan isi dengan format yang sesuai')

option = st.selectbox(
    'Jenis larutan',
    ('asam kuat', 'asam lemah', 'basa kuat','basa lemah'))
         
    
if option=="asam kuat":
    jumlah_digit=4
    cons = st.number_input(f'Masukan consentrasi larutan dalam Molaritas (M)',format='%.'+str(jumlah_digit)+'f')
    jumlah_digit1=0
    val = st.number_input(f'Masukan valensi larutan',format='%.'+str(jumlah_digit1)+'f')
    H=cons*val
    import numpy as np
    pH= -1 * np.log10(H)
    st.write('pH larutan',NamaLarutan,'adalah',pH)
    
elif option == "basa kuat":
    jumlah_digit=4
    cons = st.number_input(f'Masukan consentrasi larutan dalam Molaritas (M)',format='%.'+str(jumlah_digit)+'f')
    jumlah_digit1=0
    val = st.number_input(f'Masukan valensi larutan',format='%.'+str(jumlah_digit1)+'f')
    OH=cons*val 
    import numpy as np
    pOH= -1 * np.log10(OH)
    pH=14-pOH
    st.write('pH larutan',NamaLarutan,'adalah',pH)
    
elif option == "asam lemah":
    jumlah_digit=4
    cons = st.number_input(f'Masukan consentrasi larutan dalam Molaritas (M)',format='%.'+str(jumlah_digit)+'f')
    jumlah_digit1=6
    ka = st.number_input(f'Masukan ka dari larutan',format='%.'+str(jumlah_digit1)+'f')
    a = cons * ka
    import numpy as np
    H = np.sqrt(a)
    pH= -1 * np.log10(H)
    st.write('pH larutan',NamaLarutan,'adalah',pH)
    
elif option == "basa lemah":
    jumlah_digit=4
    cons = st.number_input(f'Masukan consentrasi larutan dalam Molaritas (M)',format='%.'+str(jumlah_digit)+'f')
    jumlah_digit1=6
    kb = st.number_input(f'Masukan kb dari larutan',format='%.'+str(jumlah_digit1)+'f')
    a = cons * kb
    import numpy as np
    OH = np.sqrt(a)
    pOH= -1 * np.log10(OH) 
    pOH= -1 * np.log10(OH)
    pH=14-pOH
    st.write('pH larutan',NamaLarutan,'adalah',pH)

    
st.image ("https://s4.aconvert.com/convert/p3r68-cdx67/api9n-49k4i.jpg",width=500)


    
    
    
