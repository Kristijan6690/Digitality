import axios from "axios";

let Service = axios.create({
    baseURL: "http://localhost:5000/"
});

let app = {
    async register(ime_prezime,eposta,lozinka){
        await Service.post('/register',{
            name: ime_prezime[0],
            surname: ime_prezime[1],
            email: eposta,
            password: lozinka
        })
    },

    async login(eposta,lozinka){
        let response = await Service.post('/login',{
            email: eposta,
            password: lozinka
        })
        return response.data;
    },

    async getArchives(id) {
        let response = await Service.post('/GetArchives',{
            user_id: id
        });
        return response.data;
    },

    async getDocuments(naziv_podarhive,id_korisnikove_arhive){
        let response = await Service.post('/documents',{
            subArchive_name: naziv_podarhive,
            personal_archive_id: id_korisnikove_arhive
        });
        return response.data;
    },

    async sendDocument(urlDokumenta){
        let response = await Service.post('/send_document',{
            doc_url : urlDokumenta
        })
        return response.data
    },

    async getSearchArchives(pretraga,id_korisnikove_arhive){
        let response = await Service.post('/search/lista_arhiva',{
            searchTerm : pretraga,
            personal_archive_id: id_korisnikove_arhive
        })
        return response.data;
    },

    async createSubarchive(naziv,id_korisnikove_arhive){
        await Service.post('/archives/createSubarchive', {
            archive_name : naziv,
            personal_archive_id : id_korisnikove_arhive
        })
    },

    async deleteSubarchive(id_korisnikove_arhive,id_podarhive,naziv_podarhive){
        let response = await Service.post('/archive/deleteSubarchive', {
            personal_archive_id : id_korisnikove_arhive,
            subarchive_id : id_podarhive,
            subarchive_name: naziv_podarhive
        })
        return response.data
    },

    async update_exDate(id_korisnikove_arhive,id_podarhive){
        await Service.post('/archive/UpdateExaminationDate',{
            personal_archive_id: id_korisnikove_arhive,
            subarchive_id: id_podarhive
        })
    },

    async sort_Archives(check_value,id_korisnikove_arhive){
        let response = await Service.post('/archives/SortArchives', {
            sorttype: check_value,
            personal_archive_id: id_korisnikove_arhive
        })
        return response.data;
    }
};

export { app, Service };