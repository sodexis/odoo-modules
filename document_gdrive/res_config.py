from openerp.osv import fields, osv

class knowledge_config_settings(osv.osv_memory):
    _inherit = 'knowledge.config.settings'
    _columns = {
        'document_gdrive_upload_dir': fields.char('Google Drive Upload Directory',
            help='Directory where the files will be uploaded using the Google File Picker.'),
    }
    
    def set_document_gdrive_upload_dir(self, cr, uid, ids, context=None):
        config = self.browse(cr, uid, ids[0], context=context)
        icp = self.pool.get('ir.config_parameter')
        icp.set_param(cr, uid, 'document.gdrive.upload.dir', repr(config.document_gdrive_upload_dir))
        