import axios from "axios";
import $router from '@/router'

let Service = axios.create({
    baseURL: "http://localhost:5000/"
});


Service.interceptors.request.use((request) => {
    try {
        request.headers['Authorization'] = 'Bearer ' + Auth.getToken();
    } catch (e) {
        console.error(e);
    }
    return request;
});

Service.interceptors.response.use( 
    (response) => {return response},
    (error) => {
        if (error.response.status == 401) {
            Auth.logout();
            $router.go();
        }
    }
);


let Auth = {
    async register(ime, prezime, eposta, lozinka){
        let response = await Service.post('/register',{
            name: ime,
            surname: prezime,
            email: eposta,
            password: lozinka
        })

        return response.data;
    },

    async login(eposta, lozinka){
        let response = await Service.post('/login', {email: eposta, password: lozinka})
        
        if(response.data){
            let user = response.data;
            let archives = await app.getArchives(user.email, user.archive_ids)
            
            localStorage.setItem('userArchives',JSON.stringify(archives))
            localStorage.setItem('user', JSON.stringify(user));
            
            return true
        }
        console.log("Failed to login!")
        return false
              
    },

    logout() {
        localStorage.removeItem('user');
        localStorage.removeItem('userArchives');
        localStorage.removeItem('scan_doc_data');
        localStorage.removeItem('currentUserArchive');
    },

    getToken() {
        let user = Auth.getUser();
        if (user && user.token) {
            return user.token;
        }
        else
            return null
    },

    getUser() {
        return JSON.parse(localStorage.getItem('user'));
    },

    authenticated() {
        let user = Auth.getUser();
        if (user && user.email) {
            return true;
        }
        return false;
    },

    state: {
        get user() {
            return Auth.getUser();
        },
        get authenticated() {
            return Auth.authenticated();
        },
    }
}

let app = {
    async getArchives(eposta, dostupne_arhive_korisniku) {
        let response = await Service.post('/GetArchives', {
            email: eposta,
            archive_ids: dostupne_arhive_korisniku
        });

        if (response.data){
            return response.data;
        }
        return false
    },

    async sendDocument(urlDokumenta){
        let response = await Service.post('/send_document',{
            doc_url : urlDokumenta
        })
        return response.data
    },

    async getSearchArchives(pretraga, dostupne_arhive_korisniku, id_trenutne_arhive){
        let response = await Service.post('/search/lista_arhiva',{
            searchTerm : pretraga,
            archive_ids: dostupne_arhive_korisniku,
            currentArchive_id: id_trenutne_arhive
        })
        return response.data;
    },

    async createSubarchive(naziv, id_korisnikove_arhive){
        await Service.post('/archives/createSubarchive', {
            archive_name : naziv,
            personal_archive_id : id_korisnikove_arhive
        })
    },

    async deleteSubarchive(id_korisnikove_arhive, id_podarhive){
        await Service.patch('/archive/deleteSubarchive', {
            personal_archive_id : id_korisnikove_arhive,
            subarchive_id : id_podarhive
        })
    },

    async update_exDate(id_trenutne_arhive, naziv_podarhive){
        await Service.post('/archive/UpdateExaminationDate',{
            cur_arc: id_trenutne_arhive,
            sub_arc: naziv_podarhive
        })
    },

    async sort_Archives(check_value,dostupne_arhive_korisniku,id_trenutne_arhive){
        let response = await Service.post('/archives/SortArchives', {
            sorttype: check_value,
            archive_ids: dostupne_arhive_korisniku,
            currentArchive_id: id_trenutne_arhive
        })
        return response.data;
    },

    async share_archive(eposta_share){
        let response = await Service.post('/archives/share', {email: eposta_share})
        return response.data;
    },

    async delete_shared_archive(eposta_share){
        let response = await Service.patch('/archives/shareDelete', {'foreign_email': eposta_share})
        return response.data
    },

    async add_alias(alias){
        await Service.put('/addAlias', alias)
        
        let user = Auth.getUser()
        user.alias_list.push(alias)

        localStorage.setItem('user', JSON.stringify(user));
    },

    async delete_alias(alias_oib){
        await Service.patch('/deleteAlias', {'oib': alias_oib})
        
        let user = Auth.getUser()
        user.alias_list = user.alias_list.filter(alias => alias.oib != alias_oib)

        localStorage.setItem('user', JSON.stringify(user));
    },

    async add_document_to_database(id_korisnikove_arhive,dokument){
        await Service.post('/addDocumentToDatabase',{
            personal_archive_id: id_korisnikove_arhive,
            document: dokument
        })
    },

    async changeArchiveName(id_trenutne_arhive, naziv_trenutne_arhive){
        await Service.post('/changeArchiveName',{
            archive_id: id_trenutne_arhive,
            archive_name: naziv_trenutne_arhive
        })
    },

    async getCompanyData(company_oib){
        let response = await Service.post('/getCompanyData', {'company_oib': company_oib})
        return response.data
    },

    async update_document(archive_id, document){
        let response = await Service.patch('/update_document', {
            'archive_id': archive_id,
            'document': document
        })
        return response.data        
    },

    async delete_document(archive_id, document){
        let response = await Service.patch('/delete_document', {
            'archive_id': archive_id,
            'document': document
        })
        return response.data        
    },

    async delete_user(sent_password){
        let response = await Service.post('/delete_user', {'sent_password': sent_password})
        return response.data
    }
};

export { app, Service, Auth };