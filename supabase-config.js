// Fill these in from your Supabase project: Settings → API.
// SUPABASE_ANON_KEY is safe to expose in frontend code — it's the public
// key, and Row Level Security (see supabase/schema.sql) is what actually
// controls who can read/write what. Never put the service_role key here.
window.SUPABASE_URL = 'https://YOUR-PROJECT.supabase.co';
window.SUPABASE_ANON_KEY = 'YOUR-ANON-KEY';

window.supabaseClient = window.supabase.createClient(
  window.SUPABASE_URL,
  window.SUPABASE_ANON_KEY
);
